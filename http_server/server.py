import asyncio

http_response_template = \
"""HTTP/1.1 200 OK
Content-Length: %d
Content-Type: text/html

%s"""

async def handle_http(reader, writer):
    request = await reader.readuntil(b"\n")

    if request.startswith(b"GET / "):
        html = \
        """<html>
            <body>
                <h1>Hello!</h1>
            </body>
        </html>"""

        writer.write((http_response_template % (len(html.encode("utf-8")), html)).encode("utf-8"))
        await writer.drain()

    writer.close()


async def start_server():
    server = await asyncio.start_server(handle_http, "127.0.0.1", 8888)
    async with server: await server.serve_forever()

