# Stevens Blueprint Summer Developer Challenge 2025

This is the template for the Stevens Blueprint summer developer challenge.

There are two parts to this challenge:

1. Backend

- Create API using FastAPI in Python
- Expose an endpoint that takes a string containing a city as a query
- Use this query to find the coordinates from this [Geocoding API](https://open-meteo.com/en/docs/geocoding-api)
- Serve structured weather data from [Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), which uses the coordinates from above as parameters
- Endpoint should GET `/api/v1/weather?city={city}`
- As a bonus, add parameters for start and end dates and pass that to the weather API
- Otherwise, just use static start and end dates
- Select temperature (you can do something like displaying hourly temperature on a graph, display high/low temp for the day, etc)
- Include appropriate error handling for cases such as unexpected inputs, internal errors, and missing cities

2. Frontend

- Create a React app with Typescript + Tailwind
- You are also encouraged to use a design library of your choice (Chakra, Headless, Shadcn, Ant Design, etc)
- Use Tailwind for all styling
- Allow users to input a city (as a string) and search
- As a bonus, you can also add a date range picker (keep in mind the API might be delayed by up to 5 days)
- Make all API calls to your backend with Axios
- Display the returned data in a structured format (can be a graph, grid card display, timeline, etc)
- As a bonus, allow users to input start and end dates

Finally, edit this README file and add run instructions for your project. For example, to run the frontend currently, you will need to run the following:

```
cd frontend
npm i
npm run dev
```
