# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:01:30 2021

@author: John
"""
import time
start = time.time()
lists = ["squ_list","pent_list","hex_list","hep_list","oct_list"]
import itertools
all_orders = list(itertools.permutations(lists))

tri_list = []
for x in range(45,141):
    tri_list.append(int(x*(x+1)/2))

squ_list = []
for x in range(32,100):
    squ_list.append(int(x**2))
    
pent_list = []
for x in range(26,82):
    pent_list.append(int(x*(3*x-1)/2))
    
hex_list = []
for x in range(23,70):
    hex_list.append(int(x*(2*x-1)))

hep_list = []
for x in range(21,64):
    hep_list.append(int(x*(5*x-3)/2))

oct_list = []
for x in range(19,59):
    oct_list.append(int(x*(3*x-2)))
    
for a in tri_list:
    for this_order in all_orders:    
        for b in eval(this_order[0]):
            sa = str(a)
            sb = str(b)
            if int(sa[2:])==int(sb[:2]):        
                for c in eval(this_order[1]):
                    sc = str(c)
                    if int(sb[2:])==int(sc[:2]):
                        for d in eval(this_order[2]):
                            sd = str(d)
                            if int(sc[2:])==int(sd[:2]):
                                for e in eval(this_order[3]):
                                    se=str(e)
                                    if int(sd[2:])==int(se[:2]):
                                        
                                        for f in eval(this_order[4]):
                                            sf = str(f)
                                            if int(se[2:])==int(sf[:2]):
                                                
                                                if int(sf[2:])==int(sa[:2]):
                                                    print (a+b+c+d+e+f)
print(time.time()-start)                        

      
                            
          