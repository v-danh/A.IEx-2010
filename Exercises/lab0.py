# Write the following functions:
# a. cube(number)
def cube(number):
    """
    which takes in a number and returns its cube. For example, cube(3) => 27.
    """
    return number ** 3

# print(cube(3))
# print(cube(4))


# b. factorial(n)
def factorial(n):
    """
    which takes in a non-negative integer n and returns n!, which is the product of
    the integers from 1 to n. (0! = 1 by definition.)
    """
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        raise Exception('factorial - input must not be negative')


# c. count_pattern(pattern, lst)
#def count_pattern(pattern, lst):
    """which counts the number of times a certain pattern of
    symbols appears in a list, including overlaps. So count_pattern( ('a', 'b'), ('a',
    'b', 'c', 'e', 'b', 'a', 'b', 'f')) should return 2, and
    count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a',
    'b', 'a')) should return 3
    """


#print(count_pattern(('a', 'b'),
#                    ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')))

# d. Expression depth
# depth('x') => 0
# depth(('expt', 'x', 2)) => 1
# depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))) => 2
# depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))) => 4

def depth(expr):
    if not isinstance(expr, tuple):
        return 0
    # this says: return the maximum depth of any sub-expression + 1
    return max(map(depth, expr)) + 1