
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
        return x % 2 == 1
    def squared(x):
        return x * x
    
    odds = [x for x in lst if is_odd(x)]
    squares = [squared(x) for x in odds]
    
    return sum(squares)
