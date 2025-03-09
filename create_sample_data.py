import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
n_samples = 100

data = {
    'location': np.random.choice(['Koramangala', 'HSR Layout', 'Indiranagar', 'BTM Layout', 'Whitefield'], n_samples),
    'rent': np.random.randint(8000, 25000, n_samples),
    'deposit': np.random.randint(20000, 50000, n_samples),
    'room_type': np.random.choice(['Single', 'Double', 'Triple'], n_samples),
    'furnishing': np.random.choice(['Fully Furnished', 'Semi Furnished', 'Unfurnished'], n_samples)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/pg_data.csv', index=False)
print("Sample data created successfully!")