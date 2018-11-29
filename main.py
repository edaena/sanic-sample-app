from sanic import Sanic
from sanic.response import json
from scipy.io import wavfile
import os
import io

app = Sanic()
app.config.REQUEST_TIMEOUT = 100000000

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route("/upload", methods=['POST'])
async def upload(request):
    if not os.path.exists("upload"):
        os.makedirs("upload")

    test_file = request.files.get('fieldNameHere')
    
    print(request)
    f = open("upload/"+ test_file.name,"wb")
    f.write(test_file.body)
    f.close()
    # f = io.BytesIO(test_file.body)

    return json({"status": "finished"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)