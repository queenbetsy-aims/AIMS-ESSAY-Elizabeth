import numpy as np
import itertools as it

Result_2=[] 
Result_1 = [] 
def option_value (n,T,N,alpha,r,kappa,s,K, nu, theta,sigma): 
    Delta_t = T/float(N)
   
    t=list
    x=it.chain
    for i in range(n):  
            Z = np.random.normal(loc=0.0, scale=1.0, size=1)
            sig = sigma + 1/sigma*(nu-kappa*sigma**2)*Delta_t  +theta*Z*np.sqrt(Delta_t) 
            Result_1.append(sig)  
            

    for y in range(n):  
        P=np.random.normal(loc=0.0, scale=1.0, size=1)
	dS =s*np.exp(alpha-Result_1[i]/2*Delta_t + Result_1[i]*P*np.sqrt(Delta_t)) 
	Result_2.append(dS) 
	#print(dS)
     		
    L=t(x(*[np.maximum(K-Result_2[i],0) for i in range(n)]))
    option_value= [i*np.exp(-r*T) for i in L ]
    return np.mean(option_value)
print option_value(10000000,1,100,0.5,0.1,0.4,60,100,0.4,0.5,0.01 )

#this is a dummy comment
