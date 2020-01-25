#Ido Shany - 207689746
#Omer Lindner - 313532574
def findWaitingTime(processes, n, bt, wt, quantum): 
	rem_bt = [0] * n 
	for i in range(n): 
		rem_bt[i] = bt[i] 
	t = 0  
	while(1): 
		done = True
		for i in range(n): 
			if (rem_bt[i] > 0) : 
				done = False  
				if (rem_bt[i] > quantum) : 
					t += quantum 
					rem_bt[i] -= quantum 
				else: 
					t = t + rem_bt[i] 
					wt[i] = t - bt[i] 
					rem_bt[i] = 0
		if (done == True): 
			break
def findTurnAroundTime(processes, n, bt, wt, tat): 
	for i in range(n): 
		tat[i] = bt[i] + wt[i] 

def findavgTime(processes, n, bt, quantum): 
    wt = [0] * n 
    tat = [0] * n 
    findWaitingTime(processes, n, bt, wt, quantum) 
    findTurnAroundTime(processes, n, bt, wt, tat) 
    total_tat = 0
    for i in range(n):  
        total_tat = total_tat + tat[i] 
    print("rr:mean turnaround time: {}".format(total_tat/n))
