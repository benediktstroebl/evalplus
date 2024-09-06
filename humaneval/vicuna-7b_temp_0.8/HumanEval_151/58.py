
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
    numbers = sorted(lst)
    n = 0
    for num in numbers:
        if (num % 2) != 0 and (num % 2 != -1):
            n += (num ** 2)
    return n

lst = [2, -2, 1, -1, 2, 1, 2]
print(double_the_difference(lst))