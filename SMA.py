import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#you have to dowlaad the data first
data = np.loadtxt('stock_index.txt',delimiter = ",",dtype='float')
S=[0,0,0,0];
S1=[];
L1=[];
L=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
for i in range(5,len(data)+1):
    P=0
    for j in range(i-5,i):
        P = P+(data[j]/5);
    P=list([P])
    S.extend(P)
    S1.extend(P)
    
for i in range(20,len(data)+1):
    K=0
    for j in range(i-20,i):
        K = K+(data[j]/20);
    K=list([K])
    L.extend(K)
    L1.extend(K)
X=np.linspace(1,491,491)
XS=np.linspace(5,491,487)
XL=np.linspace(20,491,472)
plt.plot(list(XS),S1,'c')
plt.plot(list(XL),L1,'b')
plt.plot(list(X),data,'r')
plt.xlabel('DAYS')
plt.ylabel('Bath')
plt.title('Stock Market Analysis')
plt.legend(('Short-SMA','Long-SMA','real time'))
plt.savefig('stock.png')
for i in range(1,len(data)):
    if L[i-1]>S[i-1] and S[i]>L[i]:
        print('buy at ', i)
    elif L[i-1]<S[i-1] and S[i]<L[i]:
        print('Sell at ', i)
        
        
