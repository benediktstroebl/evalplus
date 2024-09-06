
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
    numbers = [n for n in lst if n % 2 == 1 and n >= 0]
    return sum(n**2 for n in numbers)

print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) 
