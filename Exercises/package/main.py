# main.py

from . import lab

if __name__ == '__main__':
    print('a.')
    print('Cube =', lab.cube(3))
    print('##########')
    print('b.')
    print('Factorial1 =', lab.factorial(1))
    print('Factorial2 =', lab.factorial(2))
    print('Factorial3 = ', lab.factorial(3))
    print('##########')
    
    
    print('d.')
    print(lab.depth('x'))
    print(lab.depth(('expt', 'x', 2)))
    print(lab.depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))
    print(lab.depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))