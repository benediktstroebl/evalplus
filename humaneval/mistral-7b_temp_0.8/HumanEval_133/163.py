

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

    # you can't use for loop
    # i = 0
    # while i < len(lst):
    #     lst[i] = round(lst[i], -1)
    #     i += 1
    # return sum([lst[i]**2 for i in range(len(lst))])

    # solution
    return sum(round(i, -1)**2 for i in lst)

