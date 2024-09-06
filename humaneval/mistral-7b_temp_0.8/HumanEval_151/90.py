
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
    def is_odd(n):
        return n % 2 != 0

    def is_integer(n):
        return type(n) == int

    def is_negative(n):
        return n < 0

    def sum_squares(n):
        return n * n

    return sum(sum_squares(n) for n in filter(is_odd, filter(is_integer, filter(is_negative, lst))))
