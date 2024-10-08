
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
    lst = list(lst)
    even_squares = []
    for num in lst:
        if not isinstance(num, int) or num <= 0:
            continue
        elif num % 2 == 0:
            even_squares.append(num ** 2)
    return sum(even_squares)
