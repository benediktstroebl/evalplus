
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
    # return 0 if the list is empty
    if lst == []:
        return 0
    
    # create a list to add the squares of the odd numbers to
    squares = []

    for number in lst:
        # check if number is odd and positive
        if (number % 2 == 1) and (number >= 0):
            # add the square of the number to the list
            squares.append(number**2)
            
    # return the sum of the numbers in the list
    return sum(squares)
