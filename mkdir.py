from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#권한 인증 및 토큰 확인
SCOPES = ['https://www.googleapis.com/auth/drive'] #구글 드라이브 권한은 종류별로 있음
creds = None
#이미 발급받은 Token이 있을 때
if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#발급 받은 Token이 없거나 Access Token이 만료되었을 때
if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

 #연결 인스턴트 생성      
service = build('drive', 'v3', credentials=creds)

 #드라이브에 폴더 생성
file_metadata = {'name': 'Invoices', 'mimeType':'application/vnd.google-apps.folder'}
file = service.files().create(body=file_metadata, fields='id').execute()
print ('Folder ID: %s' % file.get('id') )

from googleapiclient.http import MediaFileUpload
file_metadata ={'name':'mkdir.py', 'parents':['1hDwsGI7wPPBLlu3u9e1O4B03i_TTtKxP']} #parents에 폴더 ID 복붙하기(구글 드라이브에서 확인 가능)
media = MediaFileUpload('mkdir.py')
file = service.files().create(body=file_metadata, media_body=media, fields='id'). execute()
print('File ID : %s' % file.get('id'))