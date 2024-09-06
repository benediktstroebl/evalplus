
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
    # Use a list comprehension to get a list of odd numbers
    odd = [x for x in lst if x % 2 != 0]
    
    # Get the sum of squares of the odd numbers
    odd_sum = [x**2 for x in odd]
    
    # Add the sum of squares of the odd numbers
    return sum(odd_sum)

print(double_the_difference([1, 3, 2, 0, -1, -2, 0, 4, -4])) 