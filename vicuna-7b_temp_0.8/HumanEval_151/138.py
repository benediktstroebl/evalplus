
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
    # if the input list is empty, return 0
    if not lst:
        return 0
    
    # sort the list in ascending order
    lst = sorted(lst)
    
    # initialize two variables to track the sum of squares of odd numbers
    sum_squares = 0
    odd_lst = []
    
    # loop through the list and add the squares of odd numbers to the odd_lst list
    for num in lst:
        if num % 2 == 1:
            odd_lst.append(num ** 2)
            # if the current number is odd, add the square to the sum_squares list
            if num % 2 != 0:
                sum_squares += num ** 2
    
    return sum_squares
