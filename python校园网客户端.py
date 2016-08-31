from urllib import request, parse
key='1234567890'
#密码加密函数
def pwdEncode(pw, key):
    pe = ''
    for n in range(len(pw)):
        
        ki = ord(key[len(key)- n % len(key) -1])^ord(pw[n])
        _l = chr((ki & 0x0F) + 0x36)
        _h = chr((ki >> 4 & 0x0F) + 0x63)
        if (n % 2==0) :
            pe = pe + _l + _h
        else:
            pe = pe + _h + _l 
    return pe
#用户名加密函数
def usernameEncode(username):
    name=''
    for x in username:
        x=ord(x)+4
        x=chr(x)
        name+=x
    return name
#登录函数
def login(username,password):
    login_data = parse.urlencode([('action','login'),
                              ('username','{SRUN3}\r\n'+username),
                              ('password',password),
                              ('drop','0'),
                              ('pop','1'),
                              ('type','2'),
                              ('n','117'),
                              ('mbytes','0'),
                              ('minutes','0'),
                              ('ac_id','1'),
                              ('mac','')
                              ])
    req = request.Request('http://172.16.154.130:69/cgi-bin/srun_portal')
    req.add_header('User-Agent', 'Java/1.8.0_73')
    req.add_header('Host','172.16.154.130:69')
    req.add_header('Connection','keep-alive')
    req.add_header('Accept','text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2')
    req.add_header('Accept-Encoding','utf-8')
    with request.urlopen(req,data=login_data.encode('utf-8')) as f:
       print('Data:', f.read().decode('utf-8'))
#注销函数
def logout(username):
    logout_data = parse.urlencode([('action','logout'),
                              ('username','{SRUN3}\r\n'+username),
                              ('type','2'),
                              ('mac',''),
                              ('ac_id','1')
                              ])
    req = request.Request('http://172.16.154.130:69/cgi-bin/srun_portal')
    req.add_header('User-Agent', 'Java/1.8.0_73')
    req.add_header('Host','172.16.154.130:69')
    req.add_header('Connection','keep-alive')
    req.add_header('Accept','text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2')
    req.add_header('Accept-Encoding','utf-8')
    with request.urlopen(req,data=logout_data.encode('utf-8')) as f:
        print('Data:', f.read().decode('utf-8'))
         #print('Status:', f.status, f.reason)
         #for k, v in f.getheaders():
          # print('%s: %s' % (k, v))
         
#判断是否要注销    
def isWord(username):
    word=input()
    if (word == "exit"):
        print('Logout to srun...')
        logout(username)
    else:
        print('错误输入，若要退出登录状态请再次输入exit')
        isWord(username)
#主函数   
def main():
    print('Please enter your username')
    username=input();
    username=usernameEncode(username)
    print('Please enter your password')
    password=input();
    password=pwdEncode(password, key)
    print("login to Srun.....")
    login(username,password)
    
    print("若要退出登录状态请输入exit")
    isWord(username)

if __name__ == '__main__':
    main()

        
    
 

