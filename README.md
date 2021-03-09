# QtDesktopThread
QtDesktopThread is an expansion on [DesktopThread](https://github.com/TidOS/DesktopThread).  It is largely the same, but features a Qt frontend.  
It requires:

 - python 3
 - selenium
 - chromedriver + chrome
 - pyqt5

It is highly recommended to have a [4chan pass](https://www.4channel.org/pass) so that you can use the headless mode and not have to solve a captcha in an unthemed browser.

# Setup
1. First, copy sample.cfg to desktopthread.cfg  
2. Edit desktopthread.cfg to suit your tastes  
3. Get [chromedriver](https://chromedriver.chromium.org) and make sure it is in your PATH variable, make sure chrome is insta  
lled  
4. Install the required modules with pip  
`pip install -r requirements.txt`
5. Run the script and hope it works.

You can edit the config from within the program, but for now it does not store it in a smart place and requires a good configuration before the script will run.  In the future it should not be required to copy over a sample config first but the tool is still in the very early stages and it's required for now.

# Usage  
As of now...  
  

    usage: DesktopThread.py [-h] [-G] [-F FILE] [-N NAME] [-S SUB] [-C COMMENT] [-T] [-X] [-D]  
      
    Post desktop on /g/  
      
    optional arguments:  
    -h, --help show this help message and exit  
    -G, -g, --gold sign into 4chan gold  
    -F FILE, -f FILE, --file FILE  
    absolute path to file for upload, overrides config file  
    -N NAME, -n NAME, --name NAME  
    Name to use when posting  
    -S SUB, -s SUB, --sub SUB  
    Subject to use if a new thread is made  
    -C COMMENT, -c COMMENT, --comment COMMENT  
    Comment to use when posting  
    -T, -t, --new Post a new thread even if one exists  
    -X, -x, --headless Enable headless mode for webdriver 

Generally, items in your config file should be overridden by the commandline flags. If it's not working correctly, set the op  
tion in the config file and do not use commandline flag. Headless mode can only be used when using a 4chan pass. 
  
If using captcha, solve the captcha and paste the verification into the box underneath where it shows you. The script will po  
st instantly after.
