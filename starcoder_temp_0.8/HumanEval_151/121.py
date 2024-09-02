
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
    def add_squares(lst):
        total = 0
        for i in lst:
            if i < 0 or i % 1 == 0:
                total += i*i
        return total
    
    return add_squares(lst) - add_squares(list(filter(lambda x: x%2==0, lst)))
