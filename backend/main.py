from fastapi import FastAPI

app = FastAPI()

@app.get('/api/v1/weather')
async def fetch_weather_data(city: str):
    # TODO: fetch weather data
    pass