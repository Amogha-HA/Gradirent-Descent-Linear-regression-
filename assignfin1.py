from numpy import *
import numpy as np
import csv

trainpath = "train.csv"
testpath = "test.csv"
learningRate = 0.005
# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, pointx,pointy):
    totalError = 0
    for i in range(len(pointx)):
        x = pointx[i]
        y = pointy[i]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(pointx))

def step_gradient(b_current, m_current, pointx,pointy, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(pointx))
    for i in range(len(pointx)):
        x = pointx[i]
        y = pointy[i]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(pointx,pointy, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, pointx,pointy, learning_rate)
    return [b, m]

def run():
    points = genfromtxt(trainpath, usecols = (5,1), skip_header = 1, delimiter = ",")
    pointx = genfromtxt(trainpath,usecols = (5),skip_header = 1, delimiter=",")
    pointy = genfromtxt(trainpath,usecols = (1),skip_header = 1, delimiter=",")
    a = np.min(pointx)
    g = np.max(pointx)
    h = np.min(pointy)
    j = np.max(pointy)
    n = len(pointx)
    for i in range(10000):
        pointx[i] = (pointx[i] - a)/(g-a)
        pointy[i] = (pointy[i] - h)/(j-h)
    print (pointy)
    learning_rate = 0.005
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 100000
    print ("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, pointx,pointy)))
    print ("Running...")
    [b, m] = gradient_descent_runner(pointx,pointy, initial_b, initial_m, learning_rate, num_iterations)
    print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, pointx,pointy)))
    testpoint = genfromtxt(testpath, usecols = (4), skip_header = 1, delimiter = ",")
    tpointid = genfromtxt(testpath, usecols = (0), skip_header = 1, delimiter = ",")
    ha = np.min(testpoint)
    ja = np.max(testpoint)
    n = len(testpoint)
    for i in range(n):
        testpoint[i] = (testpoint[i] - ha)/(ja-ha)
        #pointy[i] = (pointy[i] - h)/(j-h)
    myFile = open('outputpart1.2.csv', 'w',newline='')
    with myFile:  
        myFields = ['id', 'price']
        writer = csv.DictWriter(myFile, fieldnames=myFields)    
        writer.writeheader()
        for i in range (len(testpoint)):
            z = m*testpoint[i] + b
            z = z*(j-h)
            z = z + h
            writer.writerow({'id' : int(tpointid[i]), 'price': z1})
        #if i<100:
         #   print(z)
        #myfile = open('s3','w')
        #with myfile:
        #    writer = csv.writer(myfile)
        #    writer.writerow(z)
         #   writer.writerow(",")
        #if i<100:
        print (z)
if __name__ == '__main__':
    run()
