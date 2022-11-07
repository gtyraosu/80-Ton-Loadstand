import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import glob2
from matplotlib.backends.backend_pdf import PdfPages
import os
for name in glob2.glob('*.csv'):
    print(name)
    x,y=[[],[]]
    file1, ext=os.path.splitext(name)
    Filename=str(file1)+'.csv'
    df=pd.read_csv(Filename,skiprows=12)
    columns=df.dtypes.index
    Psuc=np.array(df[columns[0]])
    Tsuc=np.array(df[columns[1]])
    Pdis=np.array(df[columns[2]])
    Tdis=np.array(df[columns[3]])
    DT_sup=np.array(df[columns[28]])
    DT_sub=np.array(df[columns[29]])
    w=np.array(df[columns[6]])
    # print(x,y)
    # xbar=np.nanmean(x)
    # ybar=sum(y)/len(y)
    # print(xbar,ybar)
    # xmin=min(x)
    # xmax=max(x)
    # ymin=min(y)
    # ymax=max(y)
    
    # errorx=xmax-xmin
    # plt.bar(1, xbar)
    # plt.bar(3, ybar)
    # plt.errorbar(1,xbar,yerr=([xbar-xmin],[xmax-xbar]),fmt='k',capsize=6)
    # plt.errorbar(3,ybar,yerr=([ybar-ymin],[ymax-ybar]),fmt='k',capsize=6)
    # plt.xlim(0,4)
    # plt.ylim(0,80)
    # plt.text(.5,70,'n=10')
    # plt.text(2.5,30,'n=15')
    # plt.xticks([1,3],['Before 2010','After 2010'])

    #calculate averages
    Ps_avg=np.mean(Psuc)
    Pd_avg=np.mean(Pdis)
    Ts_avg=np.mean(Tsuc)
    N=len(Psuc)
    sumPs=0
    sumTs=0
    sumPd=0

    #calculate standard deviation
    for i in range(N):
        sumPs+=((Psuc[i]-Ps_avg)**2)/(N-1)
        sumTs+=((Tsuc[i]-Ts_avg)**2)/(N-1)
        sumPd+=((Pdis[i]-Pd_avg)**2)/(N-1)
    s_x_Psuc=np.sqrt(sumPs)
    s_x_Tsuc=np.sqrt(sumTs)
    s_x_Pdis=np.sqrt(sumPd)
    print("s_x_Psuc=",s_x_Psuc)
    print("s_x_Tsuc=",s_x_Tsuc)
    print("s_x_Pdis=",s_x_Pdis)

    #Calculate random uncertainty
    s_Psuc=s_x_Psuc/np.sqrt(N)
    s_Tsuc=s_x_Tsuc/np.sqrt(N)
    s_Pdis=s_x_Pdis/np.sqrt(N)
    
    print("s_Psuc=",s_Psuc)
    print("s_Tsuc=",s_Tsuc)
    print("s_Pdis=",s_Pdis)

    #Systematic uncertainty
    sigma_sys_Ps=0.1
    sigma_sys_T=0.2
    sigma_sys_Pd=0.375

    #total uncertainty
    u_Psuc=np.sqrt((s_Psuc**2)+(sigma_sys_Ps**2))
    u_Tsuc=np.sqrt((s_Tsuc**2)+(sigma_sys_T**2))
    u_Pdis=np.sqrt((s_Pdis**2)+(sigma_sys_Pd**2))
    
    print('Psuc = ',Ps_avg,'\u00B1',u_Psuc)
    print('Tsuc = ',Ts_avg,'\u00B1',u_Tsuc)
    print('Pdis = ',Pd_avg,'\u00B1',u_Pdis)

##    data={'Psuc':[u_Psuc,], 'Tsuc':[u_Tsuc,],'Pdis':[u_Pdis,]}
##    d=pd.DataFrame(data,columns=['Psuc','Tsuc','Pdis'])
##    d.to_csv('total uncertainty.csv')
    u_Ps=[]
    sys_Ps=0.1
    limit_Ps=[]
    pct_of_tot_Psuc=[]

    u_Ts=[]
    sys_Ts=0.2
    limit_Ts=[]
    pct_of_tot_Tsuc=[]
    
    u_Pd=[]
    sys_Pd=0.375
    limit_Pd=[]
    pct_of_tot_Pdis=[]
    
    for i in range(N+1):
        Ps1=df.iloc[0:i,0]
        Ps1_avg=np.mean(Ps1)
        #Psa.append(Ps1_avg)
        std_Ps=np.std(Ps1)
        s_Ps=std_Ps/(np.sqrt(i))
        u_Pss=(np.sqrt((s_Ps**2)+(sys_Ps**2)))
        u_Ps.append(u_Pss)
        pct_of_tot_Psuc.append((s_Ps / u_Pss)*100)
        #limit_Ps.append(np.sqrt((s_Ps**2)+(sys_Ps**2))*0.9999)

        Ts1=df.iloc[0:i,1]
        Ts1_avg=np.mean(Ts1)
        std_Ts=np.std(Ts1)
        s_Ts=std_Ts/(np.sqrt(i))
        u_Tss=(np.sqrt((s_Ts**2)+(sys_Ts**2)))
        u_Ts.append(u_Tss)
        pct_of_tot_Tsuc.append((s_Ts / u_Ts[i])*100)
        #limit_Ts.append(np.sqrt((s_Ts**2)+(sys_Ts**2))*0.9999)

        Pd1=df.iloc[0:i,0]
        Pd1_avg=np.mean(Pd1)
        std_Pd=np.std(Pd1)
        s_Pd=std_Pd/(np.sqrt(i))
        u_Pdd=(np.sqrt((s_Pd**2)+(sys_Pd**2)))
        u_Pd.append(u_Pdd)
        pct_of_tot_Pdis.append((s_Pd / u_Pdd)*100)
        #limit_Pd.append(np.sqrt((s_Pd**2)+(sys_Pd**2))*0.9999)
    
    sys_P=np.ones(1000)*sys_Ps
    sys_T=np.ones(1000)*sys_Ts
    sys_Pdi=np.ones(1000)*sys_Pd
    #limit_Ps=np.ones(1000)*(sys_Ps+(sys_Ps*0.0001))
    
    t=np.arange(0,N+1)
    #plt.plot(t,u_Ps,label='total uncertainty')
    #plt.plot(t,sys_P,label='systematic uncertainty')
    #plt.plot(t,limit_Ps,label='99.99% of total')
    plt.figure(figsize=(10,6.5))
    plt.plot(t, pct_of_tot_Psuc, label = 'Suction pressure')
    plt.plot(np.ones(1000)*5, label='5% of total')
    plt.xlabel('Number of Samples', fontsize = 22)
    plt.ylabel('random uncertainty (% of total)', fontsize = 22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.legend(fontsize = 16)
    #plt.title('Uncertainty of Suction Pressure')
    plt.show()

    limit_Ts=np.ones(1000)*(sys_Ts+(sys_Ts*0.0001))
##    plt.plot(t,u_Ts,label='total uncertainty')
##    plt.plot(t,sys_T,label='systematic uncertainty')
##    plt.plot(t,limit_Ts,label='99.99% of total')
    plt.plot(t, pct_of_tot_Tsuc, label = 'Suction Temperature')
    plt.plot(np.ones(1000)*1, label='5% of total')
    plt.xlabel('Number of Samples', fontsize = 18)
    plt.ylabel('random uncertainty (% of total)', fontsize = 18)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.legend()
    plt.title('Uncertainty of Suction Temperature')
    plt.show()

    limit_Pd=np.ones(1000)*(sys_Pd+(sys_Pd*0.0001))
##    plt.plot(t,u_Pd,label='total uncertainty')
##    plt.plot(t,sys_Pdi,label='systematic uncertainty')
##    plt.plot(t,limit_Pd,label='99.99% of total')
##    plt.xlabel('Number of Samples', fontsize = 18)
##    plt.ylabel('uncertainty', fontsize = 18)
    plt.plot(t, pct_of_tot_Pdis, label = 'Discharge pressure')
    plt.plot(np.ones(1000)*1, label='5% of total')
    plt.xlabel('Number of Samples', fontsize = 18)
    plt.ylabel('random uncertainty (% of total)', fontsize = 18)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.legend()
    plt.title('Uncertainty of Discharge Pressure')
    plt.show()
