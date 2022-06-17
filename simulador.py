import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from controlador_difuso import *

CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

# Simula el modelo del carro-pendulo.
# Parametros:
#   t_max: tiempo maximo (inicia en 0)
#   delta_t: incremento de tiempo en cada iteracion
#   theta_0: Angulo inicial (grados)
#   v_0: Velocidad angular inicial (radianes/s)
#   a_0: Aceleracion angular inicial (radianes/s2)

# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador

def simular(t_max, delta_t, theta_0, v_0, a_0):
  theta = (theta_0 * np.pi) / 180
  v = v_0
  a = a_0
  
  #Dominios
  dominio = (90 * np.pi) / 180
  theta_dominio=(-dominio,dominio)
  omega_dominio=(-3,3)
  fuerza_dominio=(-300,300)

  #Difusion
  theta_difuso=controlador_difuso(theta_dominio) 
  omega_difuso=controlador_difuso(omega_dominio)
  fuerza_difusa=controlador_difuso(fuerza_dominio)
  
  theta_part_dif=theta_difuso.particion_difusa()
  omega_part_dif=omega_difuso.particion_difusa()
  fuerza_part_dif=fuerza_difusa.particion_difusa()

  #Simular
  y = [] #posicion
  velocidad=[]
  fuerza=[]

  x = np.arange(0, t_max, delta_t)
  f=0
  for t in x:
    a = calcula_aceleracion(theta, v, -f)
    v = v + a * delta_t
    velocidad.append(v)
    theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
    y.append(theta*180/np.pi)
    theta_val_pert=theta_difuso.borrosificar(theta) #valor pertenencia
    omega_val_pert=omega_difuso.borrosificar(v)
    F=fuerza_difusa.fam(theta_val_pert,omega_val_pert)
    f=fuerza_difusa.desborrosificador(F)
    fuerza.append(f)

  #Gráficos
  #plt.figure(1)
  plt.subplot(1,3,1)
  plt.title("POSICIÓN ANGULAR")
  plt.xlabel("tiempo (s)")
  plt.ylabel("tita")
  plt.plot(x,y)
  plt.grid()
  
  #plt.figure(2)
  plt.subplot(1,3,2)
  plt.title("VELOCIDAD ANGULAR")
  plt.xlabel("tiempo (s)")
  plt.ylabel("tita_p")
  plt.plot(x,velocidad)
  plt.grid()
    
  #plt.figure(2)
  plt.subplot(1,3,3)
  plt.title("FUERZA")
  plt.xlabel("tiempo (s)")
  plt.ylabel("F")
  plt.plot(x,fuerza)
  plt.grid()
  
  plt.tight_layout()
  plt.show()
  

#simular(10, 0.1, 45, 0, 0)

#simular(10, 0.01, 45, 0, 0)

#simular(10, 0.001, 45, 0, 0)

#simular(10, 0.0001, 45, 0, 0) #tiempo_maximo, salto de tiempo, tita inicial, vel incial, aceleracion incial

simular(15, 0.0001, -60, 2, 0) #experimentar