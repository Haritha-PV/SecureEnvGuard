# main.py
import os

# Set environment variable (normally set outside of script, here for demo purposes)
os.environ['DB_USERNAME'] = "lapextended"
os.environ['DB_PASSWORD'] = "56ty56"

# Access environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

# Print environment variables
print("DB Username:", db_username)
print("DB Password:", db_password)
