import numpy as np
from scipy.linalg import circulant

#a = np.array([1,2,3])
#print(a)

#Exercice 01 :
#Question 01 :
A = circulant([1,5,4,3,2])
print(A)

C = circulant([0,0,0,0,1])
print(C)

#Question 02 :
#pour la puissance np.linalg.matrix_power
n = 5   
i =0 
for i in range (n):
    print (C**i)

#2eme methode
C_puissances = [np.linalg.matrix_power(C, k) for k in range(1, n)]

# Calculer la somme des puissances de C
s = sum((k * C_puissance) for k, C_puissance in enumerate(C_puissances, start=2))

# Calculer A = (I + somme_puissances)
B = (np.eye(5) + 1j**5 * s)


Verifier = np.allclose(B, C_puissances)

if Verifier:
    print("L'égalité A = I + somme(k=2 à n) kC^(k-1) est vérifiée.")
else:
    print("L'égalité A = I + somme(k=2 à n) kC^(k-1) n'est pas vérifiée.")
