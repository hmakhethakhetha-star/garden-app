# Garden Advice Generator
# This script provides gardening advice based on the season and type of plant.

# Advice dictionaries
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

SEASON_PLANT_RECOMMENDATIONS = {
    "summer": ["sunflowers", "basil", "tomatoes"],
    "winter": ["kale", "spinach", "pansies"],
}


def get_season_advice(season: str) -> str:
    """Return gardening advice based on the season."""
    return SEASON_ADVICE.get(season, "No advice for this season.")


def get_plant_advice(plant_type: str) -> str:
    """Return gardening advice based on the plant type."""
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def recommend_plants(season: str) -> str:
    """Recommend plants suitable for the given season."""
    plants = SEASON_PLANT_RECOMMENDATIONS.get(season)
    if plants:
        return f"Recommended plants for {season}: {', '.join(plants)}."
    return "No plant recommendations available for this season."


def generate_advice(season: str, plant_type: str) -> str:
    """Generate combined gardening advice."""
    advice = get_season_advice(season) + "\n"
    advice += get_plant_advice(plant_type) + "\n"
    advice += recommend_plants(season)
    return advice


# Main program
if __name__ == "__main__":
    season = input("Enter the season (e.g., summer, winter): ").lower()
    plant_type = input("Enter the type of plant (e.g., flower, vegetable): ").lower()

    print("\n" + generate_advice(season, plant_type))

