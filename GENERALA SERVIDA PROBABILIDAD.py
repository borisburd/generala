# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:46:56 2020

@author: Boris XD
"""
import numpy as np
import random   
def all_same(items):
    return all(x == items[0] for x in items)
def tirar_dados(cant_dados,tamaño_dados):
    generala=[]
    for i in range(cant_dados):
        dado=random.randint(1,tamaño_dados)
        generala.append(dado)
    return(generala)
def gen_serv(cant_dados,tamaño_dados):
    dados=[0,1]
    count=0
    while all_same(dados)==False:
        dados=tirar_dados(cant_dados,tamaño_dados)
        count+=1
    return(count)
def prob_gen_serv(cant_intentos,cant_dados,tamaño_dados):
    n_intentos=[]
    for i in range(cant_intentos):
        res=gen_serv(cant_dados,tamaño_dados)
        n_intentos.append(res)
    tiros=np.mean(n_intentos)
    prob=1/tiros
    print("Probabilidad: "+str(prob), "Cantidad de tiros: "+str(tiros))
   
x=prob_gen_serv(100000,5,6)
    
    
    
    
    


