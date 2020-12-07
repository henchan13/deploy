'''
    이름은 자유롭게 구성 가능
    wsgi라는 의미는 특정 플랫폼이 웹서비스가 가능할 때 wsgi 모듈이 지원된다(표현)
    flask, dJango => 단독으로 서비스하는 것보다, apache/ngix 라는 웹서버와 연동하여 주로 서비스한다
    apache 서버가 바라보는 엔트리 포인트 (시작되는 파이썬 파일)을 이 파일로 지정(용도)
'''
import sys
import os

# 현재 경로
cur_dir = os.getcwd()
print(cur_dir)

# 에러 출력을 표준출력으로 보낸다
sys.stdout = sys.stderr
sys.path.insert(0,cur_dir)

# 서버 가동을 위한 모듈 가져오기
from run import app as application