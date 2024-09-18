from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import __name__ as app_name
from . import __version__ as app_version
from .routers import api, www
from .settings import static_folder

app = FastAPI(name=app_name, version=app_version)
app.include_router(www.router)
app.include_router(api.router, prefix="/api")
app.mount(
    "/static",
    StaticFiles(directory=static_folder),
    name="static",
)
