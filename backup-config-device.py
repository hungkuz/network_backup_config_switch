from netmiko import ConnectHandler
import netmiko
from datetime import datetime


Router1= {
		'device_type': 'cisco_ios',
		'ip': '192.168.177.10',
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco',
		'verbose': False,
		}

Router2= {
		'device_type': 'cisco_ios',
		'ip': '192.168.177.20',
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco',
		'verbose': False,
		}

all_routers=[Router1,Router2]

#create backup filename format: hostname_IP_date_month_year

current_time=datetime.now()
current_date=current_time.strftime("%d")
current_month=current_time.strftime("%m")
current_year=current_time.strftime("%Y")

#login to router then run backup
for routers in all_routers:
 net_connect=ConnectHandler(**routers)
 net_connect.enable()

 command="copy running-config ftp://192.168.177.130/"
 send_bkp_command = net_connect.send_command_timing(command)
 if ("Address or name of remote host" in send_bkp_command):
  
  send_Enter= net_connect.send_command_timing("\n")
 
 if ("Destination filename" in send_Enter):
  index1=send_Enter.find("[")+1
  index2=send_Enter.find("]")
  router_hostname=send_Enter[index1:index2]
  send_Filename= net_connect.send_command_timing(router_hostname+"_"+current_date+"_"+current_month+"_"+current_year)
  if ("Error" in send_Filename):
   print (send_Filename)
 print("Da xong router "+router_hostname)



