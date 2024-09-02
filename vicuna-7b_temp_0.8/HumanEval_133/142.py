

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
    n = len(lst)
    # n = 4
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return lst[0]**2
    # else:
    #     while n > 0:
    #         n -= 1
    #         lst = [x**2 if round(x,0) == x else x for x in lst]
    #     return sum(lst)
    return sum(map(lambda x: x**2 if round(x,0) == x else x,lst))
