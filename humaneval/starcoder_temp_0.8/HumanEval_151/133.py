
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
    # Your code here
    sum_of_squares = 0
    sum_of_odds = 0
    for num in lst:
        if num > 0 and num % 2 == 1:
            sum_of_odds += num
        if num > 0:
            sum_of_squares += num ** 2
    if len(lst) == 0:
        return 0
    return sum_of_squares - sum_of_odds
