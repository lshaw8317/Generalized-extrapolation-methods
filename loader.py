# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:58:28 2023

@author: lshaw
"""
import pickle
import os
import numpy as np
np.set_printoptions(precision=30)

##FIGURE 1
##Two-stage psi=S_(1-a)S_a[x]
#psi[3,2]
with open(os.path.join('Coefficients',"a_ord4_k3.txt"), "rb") as outf:
    a_ord4_k3 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord4_k3.txt"), "rb") as outf:
    b_ord4_k3 = pickle.load(outf)
##psi[3,2]_s
with open(os.path.join('Coefficients',"a_ord4_k3_symp.txt"), "rb") as outf:
    a_ord4_k3_symp = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord4_k3_symp.txt"), "rb") as outf:
    b_ord4_k3_symp = pickle.load(outf)
#psi[2,2]
with open(os.path.join('Coefficients',"a_ord4_k2.txt"), "rb") as outf:
    a_ord4_k2 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord4_k2.txt"), "rb") as outf:
    b_ord4_k2 = pickle.load(outf)
    
##FIGURE 2
##Three-stage symm psi=S_aS_(1-2a)S_a[x]
#k=3
with open(os.path.join('Coefficients',"a_ord6_k3.txt"), "rb") as outf:
    a_ord6_k3 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord6_k3.txt"), "rb") as outf:
    b_ord6_k3 = pickle.load(outf)
#k=4 G71,G87
with open(os.path.join('Coefficients',"a_ord6_7187.txt"), "rb") as outf:
    a_ord6_7187 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord6_7187.txt"), "rb") as outf:
    b_ord6_7187 = pickle.load(outf)
#k=4 G87,G88
with open(os.path.join('Coefficients',"a_ord6_8788.txt"), "rb") as outf:
    a_ord6_8788 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord6_8788.txt"), "rb") as outf:
    b_ord6_8788 = pickle.load(outf)
#k=5 G71,G87,G91
with open(os.path.join('Coefficients',"a_ord6_718791.txt"), "rb") as outf:
    a_ord6_718791 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord6_718791.txt"), "rb") as outf:
    b_ord6_718791 = pickle.load(outf)
#k=5 G87,G88,G99
with open(os.path.join('Coefficients',"a_ord6_878899.txt"), "rb") as outf:
    a_ord6_878899 = pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord6_878899.txt"), "rb") as outf:
    b_ord6_878899 = pickle.load(outf)

##FIGURE 3
##Three-stage asymm psi=S_a1S_a2S_(1-a1-a2)[x]
#k=4 G_73=1/10080
with open(os.path.join('Coefficients',"a_ord6_asymm.txt"), "rb") as outf:
    a_ord6_asymm=pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord6_asymm.txt"), "rb") as outf:
    b_ord6_asymm=pickle.load(outf)
#list of a1 = a_ord6_asymm[:,0]
#list of a2 = a_ord6_asymm[:,1]

##FIGURE 4
##Five-stage symm psi=S_a1S_a2S_(1-2a1-2a2)S_a2S_a1[x]
#k=4 G91
with open(os.path.join('Coefficients',"a_ord8_91.txt"), "rb") as outf:
    a_ord8_91=pickle.load(outf)
with open(os.path.join('Coefficients',"b_ord8_91.txt"), "rb") as outf:
    b_ord8_91=pickle.load(outf)
#list of a1 = a_ord8_91[:,0]
#list of a2 = a_ord8_91[:,1]
print('Coefficents for Fig. 4, 5-stage integrator')
print(f'a1={a_ord8_91[:,0]}')
print(f'a2={a_ord8_91[:,1]}')
print(f'b={b_ord8_91}')


