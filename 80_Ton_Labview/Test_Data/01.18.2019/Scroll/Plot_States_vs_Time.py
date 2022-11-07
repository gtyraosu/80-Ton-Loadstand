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
    t=np.arange(1,1000)
    P_s=np.ones(999)*60.17
    P_d=np.ones(999)*119.1
    T_s=np.ones(999)*70
    DT_s=np.ones(999)*20
    with PdfPages('50E-90C-20S.pdf') as pdf:
        plt.figure(1)
        plt.plot(t,Psuc)
        plt.plot(t,P_s)
        plt.plot(t,P_s+0.5,'r')
        plt.plot(t,P_s-0.5,'r')
        plt.xlabel('Number of Samples')
        plt.ylabel('Suction Pressure (psi)')
        plt.title('Suction Pressure')
        pdf.savefig()
        plt.close()

        plt.figure(2)
        plt.plot(t,Pdis)
        plt.plot(t,P_d)
        plt.plot(t,P_d+0.5,'r')
        plt.plot(t,P_d-0.5,'r')
        plt.xlabel('Number of Samples')
        plt.ylabel('Discharge Pressure (psi)')
        plt.title('Discharge Pressure')
        pdf.savefig()
        plt.close()

        plt.figure(3)
        plt.plot(t,Tsuc)
        plt.plot(t,T_s)
        plt.plot(t,T_s+0.2,'r')
        plt.plot(t,T_s-0.2,'r')
        plt.xlabel('Number of Samples')
        plt.ylabel('Suction Temperature (°F)')
        plt.title('Suction Temperature')
        pdf.savefig()
        plt.close()

        plt.figure(4)
        plt.plot(t,Tsuc)
        plt.plot(t,T_s)
        plt.plot(t,T_s+1.8,'r')
        plt.plot(t,T_s-1.8,'r')
        plt.xlabel('Number of Samples')
        plt.ylabel('Suction Temperature (°F)')
        plt.title('Suction Temperature with ASHRAE Standard')
        pdf.savefig()
        plt.close()

        plt.figure(5)
        plt.plot(t,Tdis)
        plt.title('Discharge Temperature')
        pdf.savefig()
        plt.close()

        plt.figure(6)
        plt.plot(t,DT_sup)
        plt.plot(t,DT_s)
        plt.plot(t,DT_s+0.2,'r')
        plt.plot(t,DT_s-0.2,'r')
        plt.title('Superheat')
        pdf.savefig()
        plt.close()

        plt.figure(7)
        plt.plot(t,DT_sub)
        plt.title('Subcooling')
        pdf.savefig()

        plt.figure(8)
        plt.plot(t,w)
        plt.title('Compressor Speed')
        pdf.savefig()
        plt.close()

