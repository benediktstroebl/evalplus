
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
    
    # LISTS ARE IMMUTABLE IN PYTHON
    # therefore we have to create a new list from the given list
    new_list = []
    
    for i in lst:
        if type(i) == int and i >= 0:
            new_list.append(i*2)
    
    return sum(new_list)
