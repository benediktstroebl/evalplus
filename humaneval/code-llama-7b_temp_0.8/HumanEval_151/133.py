
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
    # Your code here
    # checks if the list is empty
    if len(lst) == 0:
        return 0

    # filters out only odd numbers
    odd_numbers = filter(lambda x: x % 2 == 1, lst)

    # returns the sum of odd numbers squared
    return sum(map(lambda x: x*x, odd_numbers))

