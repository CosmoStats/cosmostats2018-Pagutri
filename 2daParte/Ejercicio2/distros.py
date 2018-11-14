"""
Funciones varias para crear distribuciones de puntos
que pueden utilizarse para experimentar con las fun-
ciones de correlaciónen 2d.
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Puntos en una malla cuadriculada
def unif_cuad_dist(box_size, dist):
    X = np.arange(0.0, box_size + 1.0, dist)
    Y = np.zeros(int(box_size / dist) + 1)
    malla_x = np.arange(0.0, box_size + 1.0, dist)
    
    for x in malla_x:
        y = x * np.ones(int(box_size / dist) + 1)
        X = np.concatenate((X, malla_x), axis = None)
        Y = np.concatenate((Y, y), axis = None)
    
    return X, Y

# Distribución no uniforme de puntos sobre un disco
def disc_dist(box_size, n_points, radius, x_0, y_0):
    X = []
    Y = []
    
    for i in range(n_points):
        theta = 2.0 * math.pi * random.random()
        r = radius * random.random()
        x = x_0 + r * math.cos(theta)
        y = y_0 + r * math.sin(theta)
    
        X.append(x)
        Y.append(y)
        
    return X, Y

# Puntos sobre un disco, uniforme
def unif_disc_dist(n_points, radius, x_0, y_0):
    X = []
    Y = []
    
    for i in range(n_points):
        theta = 2.0 * math.pi * random.random()
        r = pow(random.randrange(0, radius**2, 1), 0.5)
        x = x_0 + r * math.cos(theta)
        y = y_0 + r * math.sin(theta)

        X.append(x)
        Y.append(y)
        
    return X, Y

# Puntos sobre un anillo
def anillo_dist(box_size, n_points, r_int, r_ext, x_0, y_0):
    X = []
    Y = []
    
    for i in range(n_points):
        theta = 2.0 * math.pi * random.random()
        r = r_int + (r_ext - r_int) * random.random()
        x = x_0 + r * math.cos(theta)
        y = y_0 + r * math.sin(theta)
    
        X.append(x)
        Y.append(y)
    
    return X, Y

# Dibujar una sola circunferencia
def draw_ring(x_0, y_0, radius, n_points):
    X = []
    Y = []
    delta = 2.0 * math.pi / float(n_points)
    
    for i in range(n_points):
        theta = i * delta
        x = x_0 + radius * math.cos(theta)
        y = y_0 + radius * math.sin(theta)
        
        X.append(x)
        Y.append(y)
        
    return X, Y

# Dibujar varias circunferencias con centros y
# tamaños aleatorios, sin salirse de la caja
def rand_circles_dist(box_size, n_rings, n_points_p_ring):
    radius = float(box_size) * random.random() / 2.0
    x_0 = radius + (box_size - 2.0 * radius) * random.random()
    y_0 = radius + (box_size - 2.0 * radius) * random.random()
    X, Y = draw_ring(x_0, y_0, radius, n_points_p_ring)
    
    for i in range(n_rings - 1):
        radius = float(box_size) * random.random() / 2.0
        x_0 = radius + (box_size - 2.0 * radius) * random.random()
        y_0 = radius + (box_size - 2.0 * radius) * random.random()
        x_c, y_c = draw_ring(x_0, y_0, radius, n_points_p_ring)
        X = np.concatenate((X, x_c), axis = None)
        Y = np.concatenate((Y, y_c), axis = None)
        
    return X, Y

# Dibujar varias circunferencias del mismo tamaño
# con centros aleatorios, sin salirse de la caja
def unif_circles_dist(box_size, n_rings, n_points_p_ring, r_ring):
    x_0 = r_ring + (box_size - 2.0 * r_ring) * random.random()
    y_0 = r_ring + (box_size - 2.0 * r_ring) * random.random()
    X, Y = draw_ring(x_0, y_0, r_ring, n_points_p_ring)
    
    for i in range(n_rings - 1):
        x_0 = r_ring + (box_size - 2.0 * r_ring) * random.random()
        y_0 = r_ring + (box_size - 2.0 * r_ring) * random.random()
        x_c, y_c = draw_ring(x_0, y_0, r_ring, n_points_p_ring)
        X = np.concatenate((X, x_c), axis = None)
        Y = np.concatenate((Y, y_c), axis = None)
        
    return X, Y

# Distribución aleatoria (y cuadrada) de puntos
def create_rand_dist(box_size, n_points):
    X = []
    Y = []
    
    for i in range(n_points):
        X.append(box_size * random.random())
        Y.append(box_size * random.random())
        
    return X, Y

# Función para crear histogramas DD y RR
def save_hist(x_data, y_data, box_size, bin_size):
    max_dist = math.sqrt(2.0 * box_size**2)
    n_points = len(x_data)
    distances = []
    bins = np.arange(0.0, max_dist, bin_size)
    
    for i in range(n_points - 1):
        for j in range(i + 1, n_points):
            distance = math.sqrt((x_data[i] - x_data[j])**2 + (y_data[i] - y_data[j])**2)
            distances.append(distance)
    
    histo = np.histogram(distances, bins = bins)
    return distances, histo

# Función para crear histograma DR 
def save_hist_DR(x1, y1, box_size1, x2, y2, box_size2, bin_size):
    max_dist1 = math.sqrt(2.0 * box_size1**2)
    max_dist2 = math.sqrt(2.0 * box_size2**2)
    max_dist = max(max_dist2, max_dist1)
    n1 = len(x1)
    n2 = len(x2)
    distances = []
    bins = np.arange(0.0, max_dist, bin_size)
    
    for i in range(n1 - 1):
        for j in range(i + 1, n2):
            distance = math.sqrt((x1[i] - x2[j])**2 + (y1[i] - y2[j])**2)
            distances.append(distance)
    
    histo = np.histogram(distances, bins = bins)
    return distances, histo