import numpy as np
import time


dimension = (10,10)
t1 =time.time()
m1 = np.random.randint(0,20, dimension)
m2 = np.random.randint(0,20, dimension)
result1 = np.dot(m1,m2)
tf1= time.time()-t1
print(result1)
print("Tiempo matriz 10x10: ",round(tf1, 4))

#100x100
dimension2 = (100,100)
t2 =time.time()
m4 = np.random.randint(0,20, dimension2)
m3 = np.random.randint(0,20, dimension2)
result2 = np.dot(m3,m4)
tf2= time.time()-t2
print(result2)
print("Tiempo matriz 100x100: ",round(tf2, 4))

#1000x1000
dimension3 = (1000,1000)
t3 =time.time()
m5 = np.random.randint(0,20, dimension3)
m6 = np.random.randint(0,20, dimension3)
result3 = np.dot(m5,m6)
tf3= time.time()-t3
print(result3)
print("Tiempo matriz 1000x1000: ",round(tf3, 4))

np.savetxt("result1.csv", result1, fmt="%.18g", header='MATRIZ 10X10\n')
np.savetxt("result2.csv", result2, fmt="%.18g", header='MATRIZ 100X100\n')
np.savetxt("result3.csv", result3, fmt="%.18g", header='MATRIZ 1000X1000\n')

archivo = open("archivo.txt", "w")
archivo.write("Tiempo matriz 10x10: "+str(round(tf1, 4))+"\n")
archivo.write("Tiempo matriz 100x100: "+str(round(tf2, 4))+"\n")
archivo.write("Tiempo matriz 1000x1000: "+str(round(tf3, 4))+"\n")