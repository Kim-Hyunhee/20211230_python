import pymysql
from time import sleep
# DB 연결 자체는 main.py에서 설정
# 만들어진 연결 정보를 받아서 사용해보자

db_connect = pymysql.connect(
    host = 'finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com', 
    port = 3306, 
    user = 'admin', 
    passwd = 'Vmfhwprxm!123', 
    db ='test_phone_book', 
    charset = 'utf8')


# 쿼리를 날려주는 역할
cursor = db_connect.cursor()


def print_main_menu():
    print('===== 전화번호부 =====')
    print('1. 로그인')
    print('2. 회원가입')
    print('0. 프로그램 종료')
    print('=====================')
    menu_num = int(input('메뉴 선택 : '))
    return menu_num

# 회원가입 실행 함수 - DB에 쿼리를 날려주자
# 회원가입 => users 테이블에 회원정보가 담긴 row를 추가하자  INSERT INTO 활용

def sign_up ():
    input_email = input('가입 이메일 : ')
    input_password = input('사용할 비밀번호 : ')
    input_nickname = input('사용할 닉네임 : ')
    
    # INSERT INTO 쿼리의 VALUES에 들어가도록 처리
    
    # f string으로 실제 입력된 내용을 쿼리에 반영
    # SQL (쿼리)를 짤 때는 'string' 형태로 처리를 해야하는 일이 빈번함
    # f"문장" 형태로 큰 string은 " "로 감싸자
    sql = f"INSERT INTO users (users.email, users.password, users.nickname) VALUES ('{input_email}', '{input_password}', '{input_nickname}')"
    
    cursor.execute(sql)
    db_connect.commit()  # 실제 DB에 요청하는 일
    
    print('회원 가입이 완료 되었습니다. 메인 화면으로 돌아갑니다.')
    sleep(2)
    
# 로그인 (sign in) 기능
# 아이디 / 비번을 입력 받아서 => DB에 정보가 맞는 회원이 있는지 검색
# True / False로 결과도 리턴
def sign_in():
    input_email = input('이메일 : ')
    input_pw = input('비밀번호 : ')
    
    # 아이디 / 비밀번호 "둘 다" 맞는 회원이 있는가? 조회 SELECT 쿼리
    sql = f"SELECT * FROM users WHERE users.email = '{input_email}' AND users.password = '{input_pw}'"
    
    # 조회 쿼리 실행
    cursor.execute(sql)
    
    # cursor에는 실행 결과가 표로 담겨있다 => tuple로 변환
    user_list = cursor.fetchall()
    
    # for문 => 내용 확인
    for user in user_list :
        print(user)