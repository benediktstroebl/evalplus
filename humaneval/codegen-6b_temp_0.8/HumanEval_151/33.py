
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
    
    # Iterate through the list
    # If an element is an int, square it, if odd increment the sum
    # If the element is a negative int, skip it
    # If the element is a float, skip it
    
    # If the list is empty, return 0
    # Otherwise, return the sum
    
    if len(lst) == 0:
        return 0
    
    else:
        odd_sum = 0
        
        for elem in lst:
            if isinstance(elem, int):
                if elem % 2 == 1:
                    odd_sum += elem ** 2
                else:
                    pass
            elif isinstance(elem, float):
                pass
            else:
                pass
    
    return odd_sum
