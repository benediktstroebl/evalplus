
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
    
    # double_the_difference([3,13,5,2,1,-5,-13,-18]) 
    # double_the_difference([1,3,2,0]) 
    # double_the_difference([-1,-2,0]) 
    # double_the_difference([9,-2]) 
    # double_the_difference([0]) 
    # double_the_difference([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14]) 
    
    return sum(a*a for a in lst if a < 0 or a % 2)
    # sum() is a keyword for list of values
    
    
    