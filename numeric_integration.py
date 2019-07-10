from sympy import *

print('----------------------------------------------------')
print('')
print('TORUS VOLUME CALCULATOR')
print('')
print('this python sheet is designed to compare different methods to calculate')
print('the volume of a rotated circle body, i.e. torus')
print('')

x = symbols('x') #define x as symbols

#basic informations (feel free to modify them)
circle_center_x = 0        #X-coordinate of the circle center
circle_center_y = 2        #X-coordinate of the circle center
circle_radius = 1          #radius of the circle (!!!!!! must be smaller than circle_center_y and positive)
number_of_divisions = 5    #number of divisions for the trapezoidal rule (the more the better approximation)

#function definition and bordersettings of the integral
f1 = circle_center_y + sqrt((circle_radius)**2 - (x-circle_center_x)**2)    #function 1 top part of circle
f2 = circle_center_y - sqrt((circle_radius)**2 - (x-circle_center_x)**2)    #function 2 bottom part of circle
integration_border_a = circle_center_x - circle_radius     #lower limit of the definite integral
integration_border_b = circle_center_x + circle_radius     #upper limit of the definite integral 

def printVolumes():
    printExact() #without integral
    printNormal()
    printTrapeze()
    printSimpson()

def printExact():
    print('Exact volume without numeric integration')
    volume = calcExact()
    print('Volume as float: ' + str(float(volume)))
    print('Volume exact: ' + str(volume))
    print('')

def printNormal():
    print('Normal')
    volume = calcNormal()
    print('Volume as float: ' + str(float(volume)))
    print('Volume exact: ' + str(volume))
    print('Volumedifference from exact calculation: ' + str(float(calcExact() - volume)))
    print('')
    
def printTrapeze():
    print('Trapeze rule')
    volume = calcTrapeze(number_of_divisions)
    print('Volume as float: ' + str(float(volume)))
    print('Volume exact: ' + str(volume))
    print('Volumedifference from exact calculation: ' + str(float(calcExact() - volume)))
    print('Hint: Play arount with <<number_of_divisions>> variable value for better approximation')
    print('')

def printSimpson():
    print('Simpsons rule')
    volume = calcSimpson(number_of_divisions)
    print('Volume as float: ' + str(float(volume)))
    print('Volume exact: ' + str(volume))
    print('Volumedifference from exact calculation: ' + str(float(calcExact() - volume)))
    print('Hint: Play arount with <<number_of_divisions>> variable value for better approximation')
    print('')

def calcExact():
    volume = 2 * pi**2 * circle_center_y * circle_radius**2 #V = 2 * π² * R * r²
    return volume

def calcNormal():
    s1 = integrate(f1**2, (x, integration_border_a, integration_border_b)) #s1 is the surface of the integral from f1
    s2 = integrate(f2**2, (x, integration_border_a, integration_border_b)) #s2 is the surface of the integral from f2
    volume = pi * (s1 - s2) #volume of rotation body is defined as pi * surface of the body -> body is the circle so s1 - s2
    return volume

def calcTrapeze(n):
    s1 = trapezRule(f1**2, n) #s1 is the surface of the integral from f1 with trapezerule
    s2 = trapezRule(f2**2, n) #s2 is the surface of the integral from f2 with trapezerule
    volume = pi * (s1 - s2) #volume of rotation body is defined as pi * surface of the body -> body is the circle so s1 - s2
    return volume

def trapezRule(function, n):
    h = (integration_border_b - integration_border_a) / n   # h = (b-a)/n
    Sum = 0.5 * (function.subs(x, integration_border_a) + function.subs(x, integration_border_b))
    for i in range(1, n):
        Sum += function.subs(x, (integration_border_a + i*h)) #
    Integral = h * Sum
    return Integral

def calcSimpson(n):
    s1 = simpsonRule(f1**2, n) #s1 is the surface of the integral from f1 with simpsonrule
    s2 = simpsonRule(f2**2, n) #s2 is the surface of the integral from f2 with simpsonrule
    volume = pi * (s1 - s2) #volume of rotation body is defined as pi * surface of the body -> body is the circle so s1 - s2
    return volume

def simpsonRule(function, n):
    steper = (abs(integration_border_a) + abs(integration_border_b)) / n #partial interval size
    part_border_a = integration_border_a
    part_border_b = part_border_a + steper
    Sum = 0
    for i in range(n):
        h = (part_border_a + part_border_b) / 2 # h = (a+b)/2
        Sum += ((part_border_b - part_border_a)/6) * (function.subs(x, part_border_a) + (4*function.subs(x, h)) + function.subs(x, part_border_b))
        part_border_a = part_border_b
        part_border_b += steper

    return Sum

#start programm
printVolumes()