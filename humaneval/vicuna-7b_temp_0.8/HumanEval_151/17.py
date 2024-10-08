
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
    numbers = [x for x in lst if x != 0]
    sum_of_squares = 0
    for num in numbers:
        num = abs(num)
        num_squared = num ** 2
        sum_of_squares += num_squared
    if len(numbers) % 2 == 1:
        sum_of_squares += sum_of_squares
    return sum_of_squares
