import re
def fun(pat):
    if (re.search(pat, no)):
        print('valid')
    else:
        print('invalid')
pat='((0|[+]?91)?[-]?[7-9][0-9]{8}[0])'
no=input('enter phone number')
fun(no)