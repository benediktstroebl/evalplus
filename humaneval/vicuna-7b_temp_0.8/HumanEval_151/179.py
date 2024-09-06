
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
    def _double_the_difference(lst):
        # check for negative numbers
        for i in range(len(lst)):
            if lst[i] < 0:
                return 0
        # check for non-integers
        for i in range(len(lst)):
            if not (lst[i] % 1 == 0):
                return 0
        # calculate sum of squared odd numbers
        odd_numbers = [x**2 for x in lst if x % 2 != 0]
        return sum(odd_numbers)
    return _double_the_difference(lst)
