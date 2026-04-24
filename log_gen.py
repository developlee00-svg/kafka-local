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
log_dir = './sensor_logs'
if not os.path.exists(log_dir): # 없으면 생성함.
    os.makedirs(log_dir)


# 3. 로그 발생 및 저장
def generate_logs(): 
    data = {
        # 로그 샘플 ( 고정된 장비 한 대만 지정)
        # 편의 상 시간을 제외한 모든 값은 고정함.
        "timestamp" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sensor_id" : "AI-FACTORY-001",
        "temperature" : 87.5,
        "humidity" : 42.8,
        "status" : "RUNNING"
    }

    # json 형태로 파일 기록 (한 줄에 로그 1개씩) -> dict 객체의 직렬화 처리 필요
    # 파일명 : ./sensor_logs/sensor_json.log
    # 한 줄에 JSON 객체 한 개씩 문자열로 기록(JSON Lines : JSONL)
    # a : Append -> 파일에 추가, 쓰기모드, 파일의 끝에 새로운 내용을 덧붙임
    with open(f"{log_dir}/sensor_json.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")
    # text 형태로 파일 기록(한 줄에 로그 1개씩) -> fString으로 구성함
    # 파일명 : ./sensor_logs/sensor_text.log
    text = f"[{ data["timestamp"]}] ID={data["sensor_id"]} |   TEMP:{data["temperature"]} |   HUMI:{data["humidity"]} |   STAT:{data["status"]}"
    with open(f"{log_dir}/sensor_text.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(text)+"\n")
    print(f"로그 발생 완료 {data["timestamp"]}")
# 4. 로그 발생기 가동
def main():
    try:
        while True:
            generate_logs()
            time.sleep(2)
    except KeyboardInterrupt:
        print('종료 중...')

# 5. 프로그램 시작
if __name__ == '__main__':
    print('로그 발생 시작. 종료 Ctrl+C')
    main()