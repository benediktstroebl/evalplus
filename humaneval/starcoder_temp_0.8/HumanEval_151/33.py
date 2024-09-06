
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
    
    new_list = [x for x in lst if isinstance(x, int) and x >= 0]
    
    if not new_list:
        return 0
    
    even = 0
    odd = 0
    
    for number in new_list:
        if number % 2 == 0:
            even += number ** 2
        else:
            odd += number ** 2
    
    return even - odd
