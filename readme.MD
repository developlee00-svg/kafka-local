# 주제
- kafka

# repo
- https://github.com/edu-kenshi/kafka-local.git

# 설치
```
    docker compose up -d
```

# 패키지 설치
```
pip install kafka-python
```

# CLI 모드로 테스트
```
# 접속
# 호스트  PC
PS ~\kafka-local> docker container exec -it kafka bash

# 컨테이너
root@4527e52ba5f6:/# pwd
/
root@4527e52ba5f6:/# cd /opt/kafka/bin

# 토픽 생성
# 파티션 1개로 관리, 복제본도 1개로 관리되는 토픽 생성
> kafka-topics.sh --create --topic sapcex --bootstrap-server 127.0.0.1:9092 --partitions 1 --replication-factor 1

# 토픽 전송(프로듀서의 업무)
> kafka-console-producer.sh --topic spacex --bootstrap-server 127.0.0.1:9092

# 토픽 수신(컨슈머의 업무)
> kafka-console-consumer.sh --topic spacex --bootstrap-server 127.0.0.1:9092
```