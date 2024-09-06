
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
    
    def check_if_odd(num):
        if num > 0 and num % 2 == 1:
            return True
        return False
    
    def squared(num):
        return num ** 2
    
    total = 0
    for item in lst:
        if check_if_odd(item):
            total += squared(item)
    return total
    
    
