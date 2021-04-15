import json
import sys
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

# noinspection PyUnresolvedReferences
import ssl

# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
from matplotlib.font_manager import FontProperties  # 步驟一




try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb

import numpy as np
import matplotlib.pyplot as plt


import csv

with open('台北暴力犯罪data.csv', 'r') as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)  # 讀擋頭
    print(header)
    x=1
    for row in read:
        print(row)


#=========變成圖表1==============

labels = ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109']
hp_robbery_means = [291,322,423,413,628,838,869,1020,1091,979,709,558,525,664,1549,1590,910,978,791,652,751,876,821,903,538,587,405,367,307,249,135,105,86,87,59,63,55,33,32,29]
sc_robbery_means = [263,272,309,369,453,653,579,787,885,849,584,410,513,569,726,722,506,519,417,389,459,527,478,492,331,346,268,261,245,167,119,120,90,92,66,69,52,33,34,32]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

ax = plt.subplot(221)
rects1 = ax.bar(x - width/2, hp_robbery_means, width, label='happaness') #發生搶劫案件數
rects2 = ax.bar(x + width/2, sc_robbery_means, width,label='solve case') #破獲搶劫案件數

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('cases') #案件數量
ax.set_title('Robbery analysis') #民國年分
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


#=========變成圖表2==============
labels = ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109']
hp_robbery_means = [211,200,249,246,258,267,248,256,271,236,225,200,187,141,217,205,158,132,107,59,47,86,76,62,61,59,60,57,70,50,47,50,65,55,72,66,56,67,44,29]
sc_robbery_means = [209,188,230,232,239,239,228,214,226,193,208,186,181,124,195,188,144,120,96,60,46,86,76,56,65,70,56,57,68,56,43,53,65,59,67,66,58,66,53,29]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

ax = plt.subplot(222)
rects1 = ax.bar(x - width/2, hp_robbery_means, width, label='happaness') #發生他殺案件數
rects2 = ax.bar(x + width/2, sc_robbery_means, width,label='solve case') #破獲他殺案件數

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('cases') #案件數量
ax.set_title('Homicide analysis') #民國年分
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()










#=========變成圖表3==============
labels = ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109']
hp_robbery_means = [80,72,93,120,100,136,131,125,101,123,111,107,153,141,169,208,206,220,155,149,144,125,137,137,188,172,206,216,209,219,245,220,190,228,138,85,48,23,16,10]
sc_robbery_means = [78,67,90,128,97,132,129,114,115,111,119,108,176,161,178,234,238,216,148,151,139,126,142,140,178,180,229,249,239,254,274,243,188,221,140,90,51,25,30,11]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

ax = plt.subplot(223)
rects1 = ax.bar(x - width/2, hp_robbery_means, width, label='happaness') #發生性犯罪案件數
rects2 = ax.bar(x + width/2, sc_robbery_means, width,label='solve case') #破獲性犯罪案件數

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('cases') #案件數量
ax.set_title('Ripe analysis') #民國年分
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()








#=========變成圖表4==============
labels = ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109']
hp_robbery_means = [392,396,517,608,582,496,577,465,360,398,463,335,318,261,421,371,318,324,346,43,56,69,64,46,34,39,10,11,8,8,7,6,5,4,4,4,5,7,5,3]
sc_robbery_means = [361,388,434,582,539,465,506,417,328,365,453,323,306,250,360,308,231,241,290,43,55,64,72,57,45,39,14,14,9,5,7,7,4,3,5,4,5,6,6,3]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

ax = plt.subplot(224)
rects1 = ax.bar(x - width/2, hp_robbery_means, width, label='happaness') #發生其他犯罪案件數
rects2 = ax.bar(x + width/2, sc_robbery_means, width,label='solve case') #破獲其他犯罪案件數

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('cases') #案件數量
ax.set_title('Else analysis') #民國年分
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

#fig.tight_layout()

plt.show()


##匯入====================SQL====================
import pymysql as MySQLdb             #  pip install MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")  #open
cursor = db.cursor()

#INSERT INTO `taipei criminal`(`Chinese year`, `hp_robbery`, `hp_homicide`, `hp_rape`, `hp_else`, `sc_robbery`, `sc_homicide`, `sc_rape`, `sc_else`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]')
# def funGetUbike():
#     context = ssl._create_unverified_context()
#     url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
#     req=httplib.Request(url)
#     try:
#             reponse = httplib.urlopen(req, context=context)
#             if reponse.code==200:
#                 contents = reponse.read() #.decode("UTF-8")
#                 print(contents)
#                 data = json.loads(contents)
#                 if(len(data)>1):                        # 確認是否有資料
#                     now = datetime.now()  # 現在時間
#                     current_time = now.strftime("%Y%m%d%H%M%S")  # 印出時間的格式
#                     print("現在時間 =", current_time)
#                     with open('c:\\桃園自行車'+str(current_time)+'.json', 'w') as f:   # 處存
#                         json.dump(data, f)
#
#                 #   迴圈把所有的sna , tot,sbi  印出來
#                 d = data["retVal"]
#                 for id in d:
#                     str1="INSERT INTO `ubiketaoyuan`(`id`, `sna`, `tot`, `sbi`, `lat`, `lng`, `bemp`, `act`, `sno`, `sarea`, `mday`, `ar`, `sareaen`, `snaen`, `aren`, `datetime`)"+\
#                          " VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]','[value-14]','[value-15]',[value-16])"
#                     str1=str1.replace("[value-1]", "null")
#                     str1 = str1.replace("[value-2]", str(d[id]["sna"]))
#                     str1 = str1.replace("[value-3]", str(d[id]["tot"]))
#                     str1 = str1.replace("[value-4]", str(d[id]["sbi"]))
#                     str1 = str1.replace("[value-5]", str(d[id]["lat"]))
#                     str1 = str1.replace("[value-6]", str(d[id]["lng"]))
#                     str1 = str1.replace("[value-7]", str(d[id]["bemp"]))
#                     str1 = str1.replace("[value-8]", str(d[id]["act"]))
#                     str1 = str1.replace("[value-9]", str(d[id]["sno"]))
#                     str1 = str1.replace("[value-10]", str(d[id]["sarea"]))
#                     str1 = str1.replace("[value-11]", str(d[id]["mday"]))
#                     str1 = str1.replace("[value-12]", str(d[id]["ar"]))
#                     str1 = str1.replace("[value-13]", str(d[id]["sareaen"]).replace("'","-"))   # '
#                     str1 = str1.replace("[value-14]", str(d[id]["snaen"]).replace("'","-"))
#                     str1 = str1.replace("[value-15]", str(d[id]["aren"]).replace("'","-"))
#                     str1 = str1.replace("[value-16]", "now()")
#                     print(str1)
#                     cursor.execute(str1)
#                     db.commit()
#                     print("站名:", d[id]["sna"], "所有數量:", d[id]["tot"], "可借數量:",