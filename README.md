# Banglore PG Data Analysis Project 🏠

## Overview
An interactive dashboard for analyzing Paying Guest (PG) accommodations using Python and Streamlit. The project provides comprehensive insights into PG data through visualizations and filters.

## Tech Stack
- **Python 3.11**
- **Core Libraries**:
  - Streamlit (v1.32.0) - Interactive dashboard
  - Pandas (v2.2.1) - Data manipulation
  - NumPy (v1.26.4) - Numerical computations
  - Matplotlib (v3.8.3) - Static visualizations
  - Seaborn (v0.13.2) - Statistical visualizations
- **Version Control**: Git
- **IDE**: Visual Studio Code

## Project Structure
```
pg-analysis/
├── data/                  # Data directory
│   └── pg_data.csv       # PG accommodation dataset
├── app.py                # Main Streamlit application
├── create_sample_data.py # Data generation script
└── requirements.txt      # Project dependencies
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Sample Data
```bash
python create_sample_data.py
```

### 4. Run Application
```bash
streamlit run app.py
```

## Data Schema

| Column | Description | Data Type | Range/Values |
|--------|-------------|-----------|--------------|
| location | Area of PG | string | Koramangala, HSR Layout, etc. |
| rent | Monthly rent | int | ₹8,000-₹25,000 |
| deposit | Security deposit | int | ₹20,000-₹50,000 |
| room_type | Sharing type | string | Single/Double/Triple |
| furnishing | Furnishing status | string | Fully/Semi/Unfurnished |
| gender | Allowed gender | string | Male/Female/Unisex |
| rating | PG rating | float | 3.0-5.0 |
| amenities | Available facilities | string | WiFi, AC, Gym, etc. |

## Features

### 1. Interactive Filters
- Location selection dropdown
- Price range slider
- Room type filter
- Gender preference filter
- Rating-based filtering

### 2. Analytics Dashboard
- **Summary Metrics**
  - Total available PGs
  - Average rent by location
  - Location distribution
  - Occupancy statistics
- **Visualizations**
  - Rent distribution histogram
  - Location-wise average rent bar chart
  - Room type distribution pie chart
  - Rating analysis heatmap
- **Data Export**
  - Interactive data table
  - CSV export functionality

### 3. Analysis Features
- Price trend analysis by location
- Amenity distribution analysis
- Gender preference patterns
- Rating correlation with rent
- Occupancy trends

## Development Guidelines

### Code Style
- Follow PEP 8 conventions
- Include docstrings and type hints
- Comment complex logic
- Use meaningful variable names

### Error Handling
- Validate all input data
- Handle missing data gracefully
- Provide user-friendly error messages
- Implement proper exception handling

### Performance Optimization
- Cache expensive computations
- Optimize data operations
- Use efficient data structures
- Implement lazy loading where appropriate

## Future Enhancements

### 1. Advanced Analytics
- Predictive pricing models
- Trend forecasting
- Occupancy prediction
- Sentiment analysis of reviews

### 2. Feature Additions
- Interactive map visualization
- Booking management system
- User authentication
- Review and rating system
- Mobile responsiveness

### 3. Technical Improvements
- Database integration (SQL/NoSQL)
- RESTful API development
- Automated testing suite
- CI/CD pipeline
- Performance monitoring

## Getting Started
1. Clone the repository
2. Set up virtual environment
3. Install dependencies
4. Generate sample data
5. Run the application
6. Access dashboard at http://localhost:8501

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a pull request

## License
MIT License

## Contact
For questions and support, please open an issue in the GitHub repository.