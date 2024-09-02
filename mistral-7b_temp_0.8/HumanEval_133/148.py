

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """

    # set a variable to hold the result
    sum_result = 0

    # convert the list to a list of ints
    for num in lst:
        # add the square of the number to the result variable
        sum_result += int(num) ** 2

    # return the result
    return sum_result
