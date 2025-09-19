from fastapi import FastAPI

catalogo = {
    "tomatoes": {
        "units": "boxes",
        "qty": 1000
    },
    "wine": {
        "units": "bottles",
        "qty": 500
    }
}

app = FastAPI( title = "New Jersey API Server" )

@app.get("/warehouse/{product}")
async def load_truck(product, order_qty):

    catalogo[product]["qty"] -= int(order_qty)
    return { 
        "product": product,
        "order_qty": order_qty,
        "units": catalogo[product]["units"],
        "remaining_qty": catalogo[product]["qty"], 
    }

