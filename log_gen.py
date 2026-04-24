'''
    - 로그를 생성해서 파일에 기록함.
    - json 형태, text(한줄에 로그기록 작성) 형태
'''

# 1. 모듈 가져오기
import json
import time
import datetime
import os

# 2. 로그가 저장되는 디렉토리 생성/지정
log_dir = './sensor_log'
if not os.path.exists(log_dir): # 없으면 생성함.
    os.makedirs(log_dir)


# 3. 로그 발생 및 저장
def generate_logs():
    pass

# 4. 로그 발생기 가동
def main():
    pass

# 5. 프로그램 시작
if __name__ == '__main__':
    print('로그 발생 시작. 종료 Ctrl+C')
    main()