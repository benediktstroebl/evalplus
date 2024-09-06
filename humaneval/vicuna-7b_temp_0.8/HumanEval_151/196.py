
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
    # Check for negative or non-integer numbers
    for i in range(len(lst)-1):
        if lst[i] < 0 or not lst[i] % 1 == 0:
            return 0
    
    # Check for odd numbers
    odd_numbers = [i for i in lst if i % 2 != 0]
    result = 0
    for odd_number in odd_numbers:
        result += (odd_number ** 2)
    
    return result
