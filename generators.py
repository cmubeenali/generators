import time, random

def do_recharge(id):
    number=random.randint(6200000000,9999999999)
    number='+91'+str(number)
    start_time=time.time()
    while time.time()-start_time<10:
        print(id+': '+'recharging '+number)
        yield False
    print(id+': '+number+' is recharged')
    yield True

def fetch_plans(id):
    start_time=time.time()
    while time.time()-start_time<3:
        print(id+' : fetching plans')
        yield False
    print(id+' : plan fetched')
    yield True

i=0
curr_routine=0
arr_running_tasks=[]
event_loop_start_time=time.time()
while True:
    time.sleep(1)
    for r_task in arr_running_tasks:
        if r_task['done']==False:
            t_res= next(r_task['task_handle'])
            if t_res:
                arr_running_tasks.remove(r_task)
                if r_task['task_code']==0:
                    curr_routine=0
                else:
                    curr_routine=1
            else:
                curr_routine=1        
        else:
            arr_running_tasks.remove(r_task)
    task=None
    if curr_routine==0:
        task= do_recharge('task_'+str(i))
    else:
        task= fetch_plans('task_'+str(i))
    res_task= next(task)
    arr_running_tasks.append({'name':'task_'+str(i),'task_code':curr_routine,'task_handle':task,'done':res_task})    
    if time.time()-event_loop_start_time>=30:
        break
    i+=1