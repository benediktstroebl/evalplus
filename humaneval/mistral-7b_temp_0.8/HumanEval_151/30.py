
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

    # iterate through the list, return the value of sum_square if number is odd
    # else return 0
    # if the number is negative or not integer, return 0

    if not lst:
        return 0

    sum_square = 0
    for i in lst:
        if i % 2 == 1 and i >= 0:
            sum_square += i ** 2

    return sum_square

