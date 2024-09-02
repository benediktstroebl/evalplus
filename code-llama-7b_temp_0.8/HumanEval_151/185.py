
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    squares = []
    for item in lst:
        if item % 2 == 0 or item > 0:
            squares.append(item**2)
    return sum(squares)
    
    '''
    import math

    def double_the_difference(lst):
        sum = 0
        for item in lst:
            if item % 2 == 0 or item > 0:
                sum += (item**2)
        return sum

    def double_the_difference(lst):
        return sum([(x**2) for x in lst if x % 2 == 0 or x > 0])

    def double_the_difference(lst):
        return sum(x**2 for x in lst if x % 2 == 0 or x > 0)
    '''
