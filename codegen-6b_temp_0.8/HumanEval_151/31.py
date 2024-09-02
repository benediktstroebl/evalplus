
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
    # List cannot be empty.
    if not lst:
        return 0
    
    # Iterate through list and add up the square of each number in list
    sums = 0
    for i in lst:
        if isinstance(i, int):
            sums += i * i
    
    # Return the sum of the sums squared.
    return sums

