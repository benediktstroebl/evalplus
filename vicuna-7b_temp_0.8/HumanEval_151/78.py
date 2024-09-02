
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
    def is_odd(num):
        return num % 2 == 1
    
    def process(lst):
        for num in lst:
            if is_odd(num) and num >= 0:
                lst.remove(num)
                lst.insert(lst.index(num) + 1, num)
        return lst
    
    return process(lst)