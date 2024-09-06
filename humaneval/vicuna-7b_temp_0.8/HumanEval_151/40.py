
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
    return sum(x**2 for x in lst if x > 0 and not(x % 1) and not(x % 3) and not(x % 2))

lst = [3, 2, -2, 4, 5, -5, 0, -3, 6]
print(double_the_difference(lst))

