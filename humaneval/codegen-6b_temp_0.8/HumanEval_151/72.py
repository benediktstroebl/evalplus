
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
    # Make sure the input list is not empty.
    if len(lst) < 1:
        return 0
    
    # Set up accumulator
    zero_sum = 0
    
    # Iterate through the list and add the square of the difference of the
    # element and the previous number to the accumulator.
    for num in lst:
        try:
            zero_sum += (num - lst[lst.index(num) - 1]) ** 2
        except IndexError:
            continue
    
    # Return the sum
    return zero_sum
