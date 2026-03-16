# NASA APOD Daily Background

Python script that fetches NASA's Astronomy Picture of the Day (APOD) and saves the HD image to your home directory for use as a desktop background.

## Prerequisites

- Python 3.x
- NASA API key (free from https://api.nasa.gov/)

## Setup

1. Install dependencies:
```bash
pip install requests
```

2. Create a `config.py` file:
```python
api_key = "YOUR_NASA_API_KEY"
home_dir = "/path/to/save/directory/"
```

## Run

```bash
python NASADailyProgram.py
```

The script will download today's APOD image in HD quality to your configured directory with the image title as the filename.

## API

Uses the NASA APOD API: `https://api.nasa.gov/planetary/apod`
