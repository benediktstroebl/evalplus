
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
    # Find all odd numbers in the list
    odd_nums = [x for x in lst if x % 2 != 0]
    
    # If the list is empty, return 0
    if not odd_nums:
        return 0
    
    # Find the sum of squares of odd numbers
    sum_of_squares = sum([(x**2) for x in odd_nums])
    
    # If the input list only contains one odd number, return its square
    if not odd_nums:
        return sum_of_squares
    
    # Otherwise, return the sum of squares of odd numbers
    return sum_of_squares
