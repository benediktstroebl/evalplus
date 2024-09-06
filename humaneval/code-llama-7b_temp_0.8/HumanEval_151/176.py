
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
    # Base case
    # when we hit base case, we return the solution
    if len(lst) == 0:
        return 0
    else:
    # Recursive case
        # we use if statements to check the edge cases
        # then we use math to get the solution
        # then we call the function with the values of the recursive cases
        # we add the results together
        if lst[-1] % 2 != 0:
            return lst[-1] ** 2 + double_the_difference(lst[:-1])
        else:
            return double_the_difference(lst[:-1])
