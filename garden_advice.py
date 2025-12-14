"""
Garden Advice Generator

This script provides gardening advice based on:
- The season entered by the user
- The type of plant entered by the user

This version replaces if/elif logic with dictionaries and includes
docstrings and comments for improved readability and maintainability.
"""

# ---------------------------------------------
# Advice dictionaries
# ---------------------------------------------

# Dictionary storing advice for each season
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

# Dictionary storing advice for each plant type
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

# ---------------------------------------------
# Functions
# ---------------------------------------------


def get_season_advice(season: str) -> str:
    """
    Return gardening advice based on the season.

    Parameters:
        season (str): The season entered by the user.

    Returns:
        str: Advice related to the given season.
    """
    return SEASON_ADVICE.get(season, "No advice for this season.")


def get_plant_advice(plant_type: str) -> str:
    """
    Return gardening advice based on the plant type.

    Parameters:
        plant_type (str): The type of plant entered by the user.

    Returns:
        str: Advice related to the given plant type.
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def generate_advice(season: str, plant_type: str) -> str:
    """
    Combine season and plant advice into a single formatted message.

    Parameters:
        season (str): The season entered by the user.
        plant_type (str): The type of plant entered by the user.

    Returns:
        str: A combined advice message.
    """
    season_msg = get_season_advice(season)
    plant_msg = get_plant_advice(plant_type)
    return f"{season_msg}\n{plant_msg}"


# ---------------------------------------------
# Main program
# ---------------------------------------------

if __name__ == "__main__":
    # Get user input
    season = input("Enter the season (e.g., summer, winter): ").lower()
    plant_type = input("Enter the type of plant (e.g., flower, vegetable): ").lower()

    # Print the generated advice
    print("\n" + generate_advice(season, plant_type))


