
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
    #if empty list return 0
    #if list contains negative numbers or numbers that are not integers, return 0
    #if list contains odd numbers, square it and double it
    #return sum of list of squares


    def is_odd(x):
        return not x % 2

    result = 0
    for x in lst:
        if is_odd(x):
            result += x**2
    return result
