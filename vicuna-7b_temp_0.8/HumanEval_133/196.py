

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
    # Solution below returns 29 but the correct output is 6
    # lst = [1,2,3]
    # return 1 + 4 + 9 = 14
    # lst = [1,4,9]
    # return 1 + 4 + 9 = 14
    # lst = [1,3,5,7]
    # return 1 + 3 + 5 + 7 = 16
    # lst = [1.4,4.2,0]
    # return 1.4**2 + 4.2**2 + 0**2 = 16.8 + 1.64 + 0.0 = 18.44
    # lst = [-2.4,1,1]
    # return -2.4**2 + 1**2 + 1**2 = -6 + 1 + 1 = 4
    return sum([float(x)**2 for x in lst])
