import os

cwd = os.getcwd()
#Reddit Looter
with open(cwd+"\\Bot\\Info\\client id.txt", "r")as a:
    client_id = a.readline()
    a.close()
with open(cwd+"\\Bot\\Info\\client secret.txt", "r")as b:
    client_secret = b.readline()
    b.close()
with open(cwd+"\\Bot\\Info\\user agent.txt", "r")as c:
    user_agent = c.readline()
    c.close()
with open(cwd+"\\Bot\\Info\\username.txt", "r")as d:
    username = d.readline()
    d.close()
with open(cwd+"\\Bot\\Info\\limit.txt", "r")as e:
    limits = e.readline()
    e.close()
if(limits != ""):
    limit = int(limits)
else:
    limit = 20
with open(cwd+"\\Bot\\Info\\subreddit1.txt", "r")as f:
    sub1 = f.readline()
    f.close()
with open(cwd+"\\Bot\\Info\\subreddit2.txt", "r")as n:
    sub2 = n.readline()
    n.close()
with open(cwd+"\\Bot\\Info\\subreddit3.txt", "r")as o:
    sub3 = o.readline()
    o.close()
with open(cwd+"\\Bot\\Info\\subreddit4.txt", "r")as p:
    sub4 = p.readline()
    p.close()
subre = sub1,sub2,sub3,sub4
subreddit = []
for i in subre:
    if(i!=""):
        subreddit.append(i)

#YouTube Bot
with open(cwd+"\\Bot\\Info\\gmail.txt", "r")as g:
    gmail = g.readline()
    g.close()
with open(cwd+"\\Bot\\Info\\password.txt", "r")as h:
    password = h.readline()
    h.close()
    password1 = ""
    for i in range(len(password)):
        password1 = password1+"*"
with open(cwd+"\\Bot\\Info\\link.txt", "r")as i:
    upload_button = i.readline()
    i.close()
with open(cwd+"\\Bot\\Info\\check.txt", "r")as q:
    chec= q.readline()
    q.close()
if chec != "Yes" and "No":
    with open(cwd+"\\Bot\\Info\\check.txt", "w")as q1:
        q1.write("No")
        check = "No"
else:
    check = chec

#Output Video Name
with open(cwd+"\\Bot\\Info\\intro video.txt", "r")as j:
    intro_video = j.readline()
    j.close()
with open(cwd+"\\Bot\\Info\\transition video.txt", "r")as k:
    transition_video = k.readline()
    k.close()
with open(cwd+"\\Bot\\Info\\outro video.txt", "r")as l:
    outro_video = l.readline()
    l.close()
with open(cwd+"\\Bot\\Info\\name.txt", "r")as m:
    na = m.readline()
    name = na+".mp4"
    m.close()

#Automated
with open(cwd+"\\Bot\\Info\\vid_no.txt", "r")as en:
    vid_no = en.readline()
    en.close()
    if vid_no == "":
        vid_no = 1
    num = 86400/int(vid_no)
with open(cwd+"\\Bot\\Info\\part.txt", "r")as pa:
    part = pa.readline()
    pa.close()
    if part == "":
        part = 1
    else:
        part = int(part)