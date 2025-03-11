from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Initial JSON data stored locally
current_data = {
    "temperature": 25.0,
    "humidity": 60.0,
    "rainfall": 5.0
}

# Pydantic model for the JSON data
class WeatherData(BaseModel):
    temperature: float
    humidity: float
    rainfall: float

# GET endpoint to retrieve the current weather data
@app.get("/api/weather", response_model=WeatherData)
def get_weather():
    return current_data

# PUT endpoint to update the weather data
@app.put("/api/weather")
def update_weather(data: WeatherData):
    global current_data
    current_data = data.model_dump()
    return {"message": "Weather data updated successfully", "data": current_data}
