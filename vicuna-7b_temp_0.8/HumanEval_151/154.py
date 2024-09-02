
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
        if x % 2 == 1:
            return True
        else:
            return False
        
    def even_or_odd(lst):
        return [x for x in lst if is_odd(x)]
    
    def sum_of_squares(lst):
        return sum([x ** 2 for x in even_or_odd(lst)])
    
    return sum_of_squares(lst)

print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))
