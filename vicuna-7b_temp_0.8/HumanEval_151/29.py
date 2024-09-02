
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
    lst = sorted(lst)
    if not lst:
        return 0
    elif not lst[1] % 2:
        odd = [x**2 for x in lst[::2]]
        even = [x**2 for x in lst[1::2]]
        result = sum([x if x > 0 else 0 for x in odd if x % 2 == 1])
        return result
    else:
        return 0
    
