from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json' # 초기설정 json파일 이름
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

print(dir(service))