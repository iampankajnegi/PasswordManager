PASSWORD={'abc@abc.com':'password1','pqrs@pqrs.com':'password2','xyz@xyz.com':'password3'}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage:py pw.py [account] - copy account password')
    sys.exit()
account=sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for '+ account +' coppied to clipboard.')
else:
    print('There is no account named'+ account)

