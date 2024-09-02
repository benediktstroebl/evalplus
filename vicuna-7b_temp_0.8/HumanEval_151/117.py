
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
    # apply the strategy of reading the list as a string and converting it
    # to a list and then converting it back to a string, with the help of str(lst)
    # and eval(str(lst))
    # eval(str(lst)) is faster than eval(lst) and it is also safer because it
    # converts the list to a string
    return eval(str(filter(int, filter(lambda x: x >= 0, list(filter(lambda x: x % 2 == 0, lst))))))