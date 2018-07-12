import paramiko
import time

# CREATE LOCAL OUTPUT FILES
fLogon = open('C:/file.log','w')
fLogout = open('C:/file.log','w')
fTestRequest = open('C:/file.log','w')
fResendRequest = open('C:/file.log','w')
fSessionLevelReject = open('C:/file.log','w')
fSequenceReset = open('C:/file.log','w')
fMarketDataRequest = open('C:/file.log','w')
fMarketDataFullRefresh = open('C:/file.log','w')
fBusinessMessageReject = open('C:/file.log','w')

# REMOTE TAGET MACHINE CONNECTION INFO
ip='10.0.0.1'
port=22
username='User'
password='UserPassword'

# UNIX COMANDS TO RUN ON TARGET MACHINE
Logon='zegrep "35=A" /*/*/*/*/fix_all.log | less'
Logout='zegrep "35=5" /*/*/*/*/fix_all.log | less'
TestRequest='zegrep "35=1" /*/*/*/*/fix_all.log | less'
ResendRequest='zegrep "35=2" /*/*/*/*/fix_all.log | less'
SessionLevelReject='zegrep "35=3" /*/*/*/*/fix_all.log | less'
SequenceReset='zegrep "35=4" /*/*/*/*/fix_all.log | less'
MarketDataRequest='zegrep "35=V" /*/*/*/*/fix_all.log | less'
MarketDataFullRefresh='zegrep "35=W" /*/*/*/*/fix_all.log | less'
BusinessMessageReject='zegrep "35=j" /*/*/*/*/fix_all.log | less'

# ESTABLISH SSH SESSION
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

# GET TARGET MESSAGES
print('GETTING Logon MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(Logon)
outlines=stdout.readlines()
resp=''.join(outlines)
fLogon.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING Logon MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING Logout MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(Logout)
outlines=stdout.readlines()
resp=''.join(outlines)
fLogout.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING Logout MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING TestRequest MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(TestRequest)
outlines=stdout.readlines()
resp=''.join(outlines)
fTestRequest.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING TestRequest MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING ResendRequest MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(ResendRequest)
outlines=stdout.readlines()
resp=''.join(outlines)
fTestRequest.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING ResendRequest MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING SessionLevelReject MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(SessionLevelReject)
outlines=stdout.readlines()
resp=''.join(outlines)
fSessionLevelReject.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING SessionLevelReject MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING SequenceReset MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(SequenceReset)
outlines=stdout.readlines()
resp=''.join(outlines)
fSequenceReset.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING SequenceReset MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING MarketDataRequest MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(MarketDataRequest)
outlines=stdout.readlines()
resp=''.join(outlines)
fMarketDataRequest.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING MarketDataRequest MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING MarketDataFullRefresh MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(MarketDataFullRefresh)
outlines=stdout.readlines()
resp=''.join(outlines)
fMarketDataFullRefresh.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING MarketDataFullRefresh MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))

print('GETTING BusinessMessageReject MESSAGES...')
start_time = time.time()
stdin,stdout,stderr=ssh.exec_command(BusinessMessageReject)
outlines=stdout.readlines()
resp=''.join(outlines)
fBusinessMessageReject.write(resp)
endTime = int(time.time() - start_time)
print('DONE GETTING BusinessMessageReject MESSAGES, TIME ELAPSED: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))