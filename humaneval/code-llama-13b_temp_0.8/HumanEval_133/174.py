

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
    # 1st solution
    # lst = [int(math.ceil(x)) ** 2 for x in lst]
    # return sum(lst)
    # 2nd solution
    # return sum(list(map(lambda x: int(math.ceil(x)) ** 2, lst)))
    # 3rd solution
    # from math import ceil
    # return sum(int(ceil(x) ** 2) for x in lst)
    # 4th solution
    # from math import ceil
    # return sum(int(ceil(x) ** 2) for x in lst)
    # 5th solution
    # return sum([int(x) ** 2 for x in map(ceil, lst)])
    # 6th solution
    from math import ceil
    return sum(ceil(x) ** 2 for x in lst)

