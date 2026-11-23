import os
from flask import Blueprint, request, send_from_directory, abort
from werkzeug.utils import secure_filename

uploads_api = Blueprint('uploads', __name__)

UPLOADS_DIR = os.path.abspath('uploads')

@uploads_api.route('/')
def get_upload():
   name = request.args.get("name", "")
   safe_name = secure_filename(name)
   if not safe_name or safe_name != name:
      abort(404)
   return send_from_directory(UPLOADS_DIR, safe_name)
