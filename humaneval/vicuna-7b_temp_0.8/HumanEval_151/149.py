
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
    numbers = [x for x in lst if x != 0]   # get all non-zero numbers in the list
    squares = [x**2 for x in numbers]   # calculate the squares of the numbers
    odd_sum = sum([x**2 for x in squares if x % 2 == 1])   # get the sum of squares of odd numbers
    return odd_sum
