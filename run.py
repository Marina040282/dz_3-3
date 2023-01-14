from flask import Flask, send_from_directory

# ����������� ���������
from app.main.views import main_blueprint
from app.loader.views import loader_blueprint

# ������� ��������� Flask
app = Flask(__name__)

# ������������ ���������
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# ������ ��� ������ ����������� � /uploads ������
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

# ��������� ������, ������ ���� ���� �������, � �� ������������
if __name__ == "__main__":
    app.run()
