
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

    # build a list of numbers with the odd numbers multiplied by 2
    # then find the sum of the numbers in the list that are odd
    numbers = []
    for num in lst:
        if num % 2 != 0:
            numbers.append(num * 2)
    return sum(numbers)

