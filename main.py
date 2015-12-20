from bottle import route, run, template
import shlex
import subprocess

@route('/theater')
def index():
    return '<a href="stream">Stream a URL</a>'

@route('/stream')
def stream():
    url_to_stream = 'http://cosmolearning.org/video-lectures/repeated-games-cheating-punishment-and-outsourcing/'

    cmd = 'sh /server/run_chrome.sh %s' %url_to_stream
    args = shlex.split(cmd)
    pipe = subprocess.Popen(args, stdout=subprocess.PIPE)	
    stdout, stderr = pipe.communicate() 
    
    return "stream a url"

@route('/upload')

def upload_file(filname):
    pass
	
run(host='10.0.0.28', port=8080)
