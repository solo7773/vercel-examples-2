from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="TTTest",
    description="test it",
    version="1.0.0",
)


@app.get("/api/data")
def get_sample_data():
    try:
        with open(ddbb.txt) as FIN:
            ccc = ','.join(FIN.readlines())
        return {'data-txt': ccc}
    except Exception:
        return {'data-err': 'error occured'}


@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    return {
        "item": {
            "id": item_id,
            "name": "Sample Item " + str(item_id),
            "value": item_id * 100
        },
        "timestamp": "2024-01-01T00:00:00Z"
    }


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ttt html</title>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
    </head>
    <body>
        <a href="page1.html">跳转</a>
    </body>
    </html>
    """
