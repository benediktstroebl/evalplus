
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
    
    # Make a new list containing the squared values of each number in lst,
    # then square the difference between them.
    squared_difference_list = [num**2 for num in lst]
    new_list = [num**2 for num in lst]
    
    # For each number in the original list, add the difference in the
    # squared list to the new list.
    for num in lst:
        new_list[lst.index(num)] += abs(num - new_list[lst.index(num)])
        
    # Return the sum of the squared differences
    return sum(new_list)
