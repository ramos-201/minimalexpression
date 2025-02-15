from starlette.applications import Starlette
from starlette.routing import Route
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='src/templates')


async def homepage(request):
    return templates.TemplateResponse(
        'index.html',
        {'request': request},
    )

app = Starlette(
    debug=True,
    routes=[Route('/', homepage)],
)
