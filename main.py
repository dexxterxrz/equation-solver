import math
import os
import platform

sys = platform.system()

def equationSolver():
    if sys == "Windows":
        os.system('cls')
    if sys == "Linux" or sys == "Darwin":
        os.system('clear')


    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))

    delta = (b*b)-(4*a*c)

    if delta < 0:
        print('Irreal result.')
        return
    
    denominatorResult = 2*a

    if delta == 0:
        numeratorResult = (b*-1)+math.sqrt(delta)
        finalResult = numeratorResult/denominatorResult
        print(f'Result: {finalResult}')

    if delta > 0:
        numeratorResult1 = (-b)+math.sqrt(delta)
        finalResult1 = numeratorResult1/denominatorResult
        print(f'Result 1: {finalResult1}')

        numeratorResult2 = (-b)-math.sqrt(delta)
        finalResult2 = numeratorResult2/denominatorResult
        print(f'Result 2: {finalResult2}')
equationSolver()