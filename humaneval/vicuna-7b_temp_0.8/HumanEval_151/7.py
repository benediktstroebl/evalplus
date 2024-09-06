
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
    def is_odd(x):
        if x % 2 == 1:
            return True
        else:
            return False
    
    def double_the_difference_helper(lst, index):
        if index == len(lst):
            return lst[index]
        if is_odd(lst[index]):
            return double_the_difference_helper(lst, index+1) + lst[index]
        else:
            return double_the_difference_helper(lst, index+1) + lst[index]**2
    
    return double_the_difference_helper(lst, 0)