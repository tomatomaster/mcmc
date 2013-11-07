import re
import random
import math
import pylab
import numpy

def target_function(x, mean, b):
	target_p = 0.0
	target_p = 1/2*b*math.exp(-math.fabs(x-mean)/b)
	return target_p

def alpha_function(x, xt):
	p = 0.0
	p = math.exp((-1/3.0)*(math.fabs(x)-math.fabs(xt)))
	return p

def random_walk(x):
	p = 0.0
	p = random.gauss(x, 3)
	return p

flag = False
sig = 0.0
e = 0.0
result = []
each_steps  = []
sample_t = 0.0


while(flag == False):
	sample = random_walk(1)
	if( alpha_function(sample, 1) >= 1):
		result.append(sample)
		sample_t = sample
		flag = True

	else:
		u = random.random() 
		if(alpha_function(sample, 10) > u):
			result.append(sample)
			sample_t = sample
			flag = True

counter = 0.0
for i in range(0, 200000):
	sample = random_walk(sample_t)
	u = random.random()
	#if( target_function(sample, 0, 3)/target_function(sample_t, 0, 3) >= 1 or (alpha_function(sample, sample_t)>u) ):
	if( (alpha_function(sample, sample_t) >= 1) or (alpha_function(sample, sample_t)>u) ):
		sample_t = sample		
		counter  +=1
		if(i > 1000):
			result.append(sample)

mean_step = []
for i,value in enumerate(result):
	e += value
	i = i+1
	mean_step.append(e/i)

mean = e/i
print mean


var_step = []
for x,value in enumerate(result):
	factor = value-mean
	sig +=  factor**2
	x = x+1
	var_step.append(sig/x)

print sig/x


pylab.grid(True)
pylab.plot(result,"r")
pylab.plot(mean_step,"b")
pylab.plot(var_step,"g")
pylab.show()
