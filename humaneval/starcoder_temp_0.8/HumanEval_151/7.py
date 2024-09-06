
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
    lst = [i for i in lst if i>=0 and type(i)==int]
    if not lst:
        return 0
    sum_of_squares = sum([i**2 for i in lst])
    sum_of_odds = sum([i for i in lst if i%2!=0])
    return 2*sum_of_odds - sum_of_squares
