from init import *

self.route("/")
async def index():
    return "Hello World"

if __name__ == "__main__":
    self.run(
        debug = True,
        host = "0.0.0.0",
        port = "8000",
    )