from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/read_example_file")
async def read_example_file():
    with open("example.txt") as contents:
        return {"contents": contents.read()}
