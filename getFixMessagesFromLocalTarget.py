import os
import time

# CREATE LISTS
listLogon = []
listLogout = []
listTestRequest = []
listResendRequest = []
listSessionLevelReject = []
listSequenceReset = []
listMarketDataRequest = []
listMarketDataFullRefresh = []
listBusinessMessageReject = []

# CREATE OUTPUT FILES
fileLogon = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgLogon.log','w')
fileLogout = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgLogout.log','w')
fileTestRequest = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgTestRequest.log','w')
fileResendRequest = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgResendRequest.log','w')
fileSessionLevelReject = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgSessionLevelReject.log','w')
fileSequenceReset = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgSequenceReset.log','w')
fileMarketDataRequest = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgMarketDataRequest.log','w')
fileMarketDataFullRefresh = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgMarketDataFullRefresh.log','w')
fileBusinessMessageReject = open('C:/Users/apanasenko/Desktop/LOGS/FixTakerLogs/MsgBusinessMessageReject.log','w')

# GET MESSAGES
path = 'C:/Users/apanasenko/Desktop/LOGS/LAS_LN_FIX_TAKER_LOGS/'
start_time = time.time()
filelist = os.listdir(path)
for file in filelist:
    if file.endswith('.log'):
        with open(path + file, 'r') as log:
            print('[STARTING DATA EXTRACTION]:')
            print('[WORKING ON]:',log)
            for line in log:
                if '35=A' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listLogon:
                        listLogon.append(line)
                        fileLogon.write(line)
                if '35=5' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listLogout:
                        listLogout.append(line)
                        fileLogout.write(line)
                if '35=1' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listTestRequest:
                        listTestRequest.append(line)
                        fileTestRequest.write(line)
                if '35=2' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listResendRequest:
                        listResendRequest.append(line)
                        fileResendRequest.write(line)
                if '35=3' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listSessionLevelReject:
                        listSessionLevelReject.append(line)
                        fileSessionLevelReject.write(line)
                if '35=4' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listSequenceReset:
                        listSequenceReset.append(line)
                        fileSequenceReset.write(line)
                if '35=V' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listMarketDataRequest:
                        listMarketDataRequest.append(line)
                        fileMarketDataRequest.write(line)
                if '35=W' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listMarketDataFullRefresh:
                        listMarketDataFullRefresh.append(line)
                        fileMarketDataFullRefresh.write(line)
                if '35=j' in line:
                    line = line.split(' ')
                    line = line[2]
                    if line not in listBusinessMessageReject:
                        listBusinessMessageReject.append(line)
                        fileBusinessMessageReject.write(line)
endTime = int(time.time() - start_time)
print('[DONE! TIME ELAPSED]: {:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60))