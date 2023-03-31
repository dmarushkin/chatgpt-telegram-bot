import os
import asyncio

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Route

import requests

TELEGRAM_BOT_TOKEN = "1111111111:AAXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

async def success_webhook(request: Request) -> PlainTextResponse:

    chat_id = request.query_params["chat_id"]

    if not os.path.isfile(f'./users/{chat_id}'):

        f = open(f'./users/{chat_id}', "w")
        f.write('1')
        f.close()

        bot_message = "You are successfully authorized!"
        send_text = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

    return PlainTextResponse("1")


async def main() -> None:

    starlette_app = Starlette(
        routes=[
            Route("/success", success_webhook, methods=["GET"]),
        ]
    )

    webserver = uvicorn.Server(
        config=uvicorn.Config(
            app=starlette_app,
            port=8000,
            use_colors=False,
            host="0.0.0.0",
        )
    )

    await webserver.serve()

if __name__ == "__main__":
    asyncio.run(main())
