
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
    # check for empty list
    if not lst:
        return 0
    
    # list of odd numbers
    odd_lst = [x for x in lst if x % 2 != 0]
    
    # calculate the sum of squares of odd numbers
    odd_sum = sum([x**2 for x in odd_lst])
    
    # calculate the sum of squares of even numbers
    even_sum = sum([x**2 for x in lst if x % 2 == 0 and x >= 0])
    
    # return the sum of squares of odd numbers
    return odd_sum - even_sum
