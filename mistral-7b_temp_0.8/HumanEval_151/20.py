
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


    # initialize a variable, sum, to store the sum of the squares of the odd numbers
    sum = 0

    # loop through the list, lst
    for number in lst:
        # check if the number is odd and if it is a number and not negative
        if not number % 2 and number >= 0:
            # add the square of the number to the sum
            sum += number * number
    return sum


