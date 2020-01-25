#!/usr/bin/python3
#Ido Shany - 207689746
#Omer Lindner - 313532574
import sys
import re
from operator import itemgetter
import rr


if len(sys.argv) != 2:
    sys.stderr.write("<usage> ./main <input>\n")
    sys.exit(1)
input_file = open(sys.argv[1] , 'r').read()
n = int(input_file.split('\n')[0])
proc = []
burst_time = []
for input_ in input_file.split('\n')[1::][:-1]:
    proc.append(re.search(r'(\d+)\,(\d+)', input_).group(1))
    burst_time.append(re.search(r'(\d+)\,(\d+)', input_).group(2))

#FCFS
def fcfs():
    sorted_stuff = [list(x) for x in zip(*sorted(zip(proc, burst_time), key=itemgetter(0)))]
    sorted_proc = sorted_stuff[0]
    sorted_burst = sorted_stuff[1]
    ft = []
    ft.append(int(sorted_proc[0]) + int(sorted_burst[0]))
    for pro, time, i in zip(sorted_proc[1::],sorted_burst[1::], range(1,n)):
        if int(pro) >  (int(ft[i-1])):
            ft.append(int(pro) + int(time))
        else:
            ft.append(int(time)+int(ft[i-1]))
    ta = []
    for pro, i in zip(sorted_proc, range(n)):
        ta.append(int(ft[i]) - int(pro))
    avg = 0
    for i in ta:
        avg += i
    avg = avg/n
    print("FCFS: mean turnaround =", avg)

def lcfs_non():
    sorted_stuff = [list(x) for x in zip(*sorted(zip(proc, burst_time), key=itemgetter(0)))]
    t = 0
    sorted_proc = sorted_stuff[0]
    sorted_time = sorted_stuff[1]
    ft = []
    ft.append(int(sorted_time[0]) + int(sorted_proc[0]))
    for pro, time, i in zip(sorted_proc[1::][::-1],sorted_time[1::][::-1], range(1,n)):
        if int(time) == 0:
            ft.append(ft[i-1])
        elif int(pro) > ft[i-1]:
            ft.append(int(pro) + int(time))
        else:
            ft.append(ft[i-1] + int(time))
    ta = []
    ta.append(sorted_time[0])
    for pro, i in zip(sorted_proc[1::][::-1], range(1,n)):
        ta.append(ft[i] - int(pro))
    avg = 0
    for t in ta:
        avg += int(t)
    avg = avg/n
    print("LCFS_non: mean turnaround =", avg)

def lcfs_p():
    for i ,time,pro in zip(range(n), burst_time,proc):
        burst_time[i] = int(time)
        proc[i] = int(pro)
    sorted_stuff = [list(x) for x in zip(*sorted(zip(proc, burst_time), key=itemgetter(1)))]
    sorted_proc = sorted_stuff[0]
    sorted_time = sorted_stuff[1]
    ft = []
    ft.append(int(sorted_time[0]) + int(sorted_proc[0]))
    for pro, time, i in zip(sorted_proc[1::][::-1],sorted_time[1::][::-1], range(1,n)):
        if int(time) == 0:
            ft.append(ft[i-1])
        elif int(pro) > ft[i-1]:
            ft.append(int(pro) + int(time))
        else:
            ft.append(ft[i-1] + int(time))
    ta = []
    ta.append(sorted_time[0])
    for pro, i in zip(sorted_proc[1::][::-1], range(1,n)):
        ta.append(ft[i] - int(pro))
    avg = 0
    for t in ta:
        avg += int(t)
    avg = avg/n
    print("LCFS_p: mean turnaround =", avg)

def RR():
    sorted_stuff = [list(x) for x in zip(*sorted(zip(proc, burst_time), key=itemgetter(0)))]
    sorted_proc = sorted_stuff[0]
    sorted_time = sorted_stuff[1]
    for pro,time,i in zip(sorted_proc, sorted_time, range(n)):
        sorted_proc[i] = int(pro)
        sorted_time[i] = int(time)
    rr.findavgTime(proc, n, sorted_time,2)
def sjf():    
    for i ,time,pro in zip(range(n), burst_time,proc):
        burst_time[i] = int(time)
        proc[i] = int(pro)
    sorted_stuff = [list(x) for x in zip(*sorted(zip(proc, burst_time), key=itemgetter(1)))]
    bt = sorted_stuff[1]
    processes = sorted_stuff[0]
    wt=[]    
    ta=[]    #tat stands for turnaround time
    avg=0   #average of total turnaround time
    wt.insert(0,0)
    ta.insert(processes[0],bt[0])
    for i in range(1,len(bt)):  
        wt.insert(i,wt[i-1]+bt[i-1])
        ta.insert(i,wt[i]+bt[i])
        avg+=ta[i]
    avg=float(avg)/n
    print("sjf: mean turnaround is: "+str(avg))

if  __name__ == '__main__':
    fcfs()
    lcfs_non()
    lcfs_p()
    RR()
    sjf()
