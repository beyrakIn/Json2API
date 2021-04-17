import os
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from json_api.settings import BASE_DIR


class JSONFileView(APIView):
    def get(self, request, filename):
        file_path = os.path.join(BASE_DIR / 'files/json', filename)
        with open(file_path) as jsonfile:
            json_data = json.loads(jsonfile.read())
        return Response(json_data)
