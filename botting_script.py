import requests
import json

# Function to fetch livestream channel info
def get_livestream_info(user_id):
    url = f"https://api-backend.parti.com/parti_v2/profile/get_livestream_channel_info/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Debug: Print full response to understand its structure
        print("API Response:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Analyze viewer data using different bot ratios
def analyze_viewer_data(data):
    # Extracting necessary fields from the nested structure
    channel_info = data.get("channel_info", {})
    stream_info = channel_info.get("stream", {})
    channel_details = channel_info.get("channel", {})

    # Get values for id and viewer_count
    user_id = channel_details.get("user_id", "Unknown")
    total_viewers = stream_info.get("viewer_count", 0)

    # 8:1 Fake-to-Real Ratio Calculation
    real_viewers_8 = total_viewers / 9
    fake_viewers_8 = (total_viewers * 8) / 9

    # 12:1 Fake-to-Real Ratio Calculation
    real_viewers_12 = total_viewers / 13
    fake_viewers_12 = (total_viewers * 12) / 13

    return {
        "id": user_id,
        "total_viewer_count": total_viewers,
        "8:1_ratio": {
            "real_viewer_count": int(real_viewers_8),
            "bot_viewer_count": int(fake_viewers_8),
        },
        "12:1_ratio": {
            "real_viewer_count": int(real_viewers_12),
            "bot_viewer_count": int(fake_viewers_12),
        }
    }

# Save data to a JSON file
def save_to_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

# Main execution
user_id = 348242

# Define the correct file path for saving the JSON file
file_path = r"bot.json"

data = get_livestream_info(user_id)
if data:
    analyzed_data = analyze_viewer_data(data)
    save_to_json(analyzed_data, file_path)
else:
    print("Failed to retrieve or process data.")
