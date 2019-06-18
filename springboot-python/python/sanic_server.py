# -*- coding: UTF-8 -*-

import json
from sanic import Sanic
from sanic import response
import logging

logger = logging.getLogger(__name__)

app = Sanic()


@app.route("/health", methods=['GET'])
async def health(request):
    result = {'status': 'UP'}
    return response.json(result)

@app.route('/', methods=['GET'])
async def get_name(request):
    logger.info(request)
    return response.json({"name": "sanic_service"})


#定义
@app.route('/responds/', methods=['POST'])
async def post_handler(request):
    request_json = request.body
    input_json = json.loads(request_json.decode('utf8'))
    logger.info(input_json)
    return response.text("连接服务成功")

    
if __name__ == "__main__":
    app.run(host="localhost", port=8400)
