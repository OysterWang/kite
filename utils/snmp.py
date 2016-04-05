#/usr/bin/python
#coding:utf-8
import os,subprocess
import datetime
import time,string,math

def printsnmpwalk():

	str_ifindex = "snmpwalk -v 2c  -c snmpsoho2000 192.168.48.10 IF-MIB::ifDescr|grep -w Port-channel1 | cut -d '=' -f 1 | cut -d '.' -f 2"
	#str_ifHCOutOctets = "snmpget -v 2c  -c snmpsoho2000 192.168.48.10 IF-MIB::ifHCOutOctets." + ifindex + " | cut -d ':' -f 4 | tr -d '[:blank:]'"
	ifindex = 0
	
	p=subprocess.Popen(str_ifindex, shell=True, stdout=subprocess.PIPE) 
	p.wait()
	print("return code:%s"%p.returncode)
	ifindex = int(p.stdout.read().strip())
	str_ifHCOutOctets = "snmpget -v 2c  -c snmpsoho2000 192.168.48.10 IF-MIB::ifHCOutOctets." + str(ifindex) + " | cut -d ':' -f 4 | tr -d '[:blank:]'"

	print("ifindex:%s" %ifindex)
	starttime = datetime.datetime.now()
	print("开始时间：%s " %starttime.strftime("%Y-%m-%d %H:%M:%S %f"))

	p=subprocess.Popen(str_ifHCOutOctets, shell=True, stdout=subprocess.PIPE) 
	p.wait()
	ifHCOutOctets_1 = int(p.stdout.read().strip())
	print("ifHCOutOctets_1:%s" %ifHCOutOctets_1)

	time.sleep(2)

	p=subprocess.Popen(str_ifHCOutOctets, shell=True, stdout=subprocess.PIPE) 
	p.wait()
	ifHCOutOctets_2 = int(p.stdout.read().strip())
	print("ifHCOutOctets_2:%s" %ifHCOutOctets_2)

	endtime = datetime.datetime.now()
	print("结束时间：%s " %endtime.strftime("%Y-%m-%d %H:%M:%S %f"))
	dur_second = (endtime - starttime).seconds
	dur_millisecond = (endtime - starttime).microseconds/1000000
	#print("经历时间(秒)：%s " %dur_second)
	#print("经历时间(毫秒)：%s " %dur_millisecond)
	dur_time = dur_second + dur_millisecond
	print("持续时间：%s秒" %dur_time)
	traffic = ifHCOutOctets_2 - ifHCOutOctets_1
	print("流量是%s Bytes,速度是%s kbps" %(traffic, int(traffic * 8 /float(dur_time))/1000))

	

	#time1 = time.time()
	#print(time.localtime(time1))
	#print("time1格式化：%s" %time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time1)))
	#time.sleep(1)
	#time2 = time.time()
	#print(time.localtime(time2))
	#print("time2 - time1 = %s"%(time2 - time1))

	#print("ifHCOutOctets结果:%s" %snmp_str)
	#return snmp_str

#os.popen('snmpwalk -c %s  -v 2c %s %s 2>/dev/null'%(publicKey,host,iso)).readlines()

#snmpwalk -v 2c  -c snmpsoho2000 192.168.48.10 IF-MIB::ifDescr|grep -w Port-channel1 | cut -d '=' -f 1 | cut -d '.' -f 2
#snmpget -v 2c  -c snmpsoho2000 192.168.48.10 IF-MIB::ifHCOutOctets.${index} | cut -d ':' -f 4 | tr -d '[:blank:]'

if __name__ == "__main__":
	

	print("3")
	printsnmpwalk()
	#print(os.popen(printsnmpwalk()).readlines())
	

