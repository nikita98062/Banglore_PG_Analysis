import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Banglore PG Analysis Dashboard",
    page_icon="🏠",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/pg_data.csv')
        return df
    except:
        st.error("Unable to load data. Please check if data file exists.")
        return pd.DataFrame()

# Main function
def main():
    st.title("🏠 Banglore PG Analysis Dashboard")
    
    # Load data
    df = load_data()
    
    if not df.empty:
        # Sidebar filters
        st.sidebar.header("Filters")
        
        # Location filter
        locations = ["All"] + sorted(df['location'].unique().tolist())
        selected_location = st.sidebar.selectbox("Select Location", locations)
        
        # Price range filter
        price_range = st.sidebar.slider(
            "Price Range",
            min_value=int(df['rent'].min()),
            max_value=int(df['rent'].max()),
            value=(int(df['rent'].min()), int(df['rent'].max()))
        )
        
        # Filter data
        filtered_df = df.copy()
        if selected_location != "All":
            filtered_df = filtered_df[filtered_df['location'] == selected_location]
        filtered_df = filtered_df[
            (filtered_df['rent'] >= price_range[0]) & 
            (filtered_df['rent'] <= price_range[1])
        ]
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total PGs", len(filtered_df))
        with col2:
            st.metric("Average Rent", f"₹{filtered_df['rent'].mean():,.2f}")
        with col3:
            st.metric("Locations Count", len(filtered_df['location'].unique()))
        
        # Visualizations
        st.header("📊 Data Analysis")
        
        # Price Distribution
        st.subheader("Rent Distribution")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=filtered_df, x='rent', bins=30)
        plt.xlabel("Rent (₹)")
        plt.ylabel("Count")
        st.pyplot(fig)
        
        # Location wise average rent
        st.subheader("Average Rent by Location")
        location_avg = filtered_df.groupby('location')['rent'].mean().sort_values(ascending=True)
        fig, ax = plt.subplots(figsize=(12, 6))
        location_avg.plot(kind='bar')
        plt.xticks(rotation=45)
        plt.xlabel("Location")
        plt.ylabel("Average Rent (₹)")
        st.pyplot(fig)
        
        # Raw data
        st.header("📑 Raw Data")
        st.dataframe(filtered_df)
        
        # Download filtered data
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download filtered data as CSV",
            data=csv,
            file_name=f"pg_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
if __name__ == "__main__":
    main()