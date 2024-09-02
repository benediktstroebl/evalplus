
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
    # if the list is empty, return 0
    if not lst:
        return 0
    
    # if the input list is a single element, that element is odd
    if not lst:
        return 0
    
    # if the input list is a single odd number, return the square of that number
    if not lst:
        return 0
    
    # if the input list has only one number, that number is odd
    if not lst:
        return 0
    
    # use a dictionary to count the number of squares of odd numbers in the list
    squares = {x**2 for x in lst if x > 0}
    odd_squares = len(squares)
    
    # if the input list is a single even number, return 0
    if not lst:
        return 0
    
    # if the input list has only one number, that number is odd
    if not lst:
        return 0
    
    # if the input list has multiple numbers, return the sum of squares of the odd numbers
    return odd_squares + (lst[0]**2 + lst[1]**2 + 2*(lst[0] + lst[1])*(lst[0] - lst[1]))
