from flask import Flask

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__)

# 기본 경로("/")에 대한 엔드포인트 정의
@app.route('/')
def home():
    return "Hello, World"

# 애플리케이션 실행
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
