
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
    # remove negative numbers and non-integers
    lst = [x for x in lst if x >= 0 and x % 1 == 0]
    # sort the list
    lst.sort()
    # initialize variables to store the sum of squares of odd numbers and the sum of squares of even numbers
    odd_sum = 0
    even_sum = 0
    # iterate through the sorted list
    for x in lst:
        # if the current number is odd
        if x % 2 != 0:
            odd_sum += x ** 2
        # if the current number is even
        else:
            even_sum += x ** 2
    return odd_sum + even_sum
