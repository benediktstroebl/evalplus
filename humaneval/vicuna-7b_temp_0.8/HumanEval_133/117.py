

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
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([1, 2, 3])
    # returns 14
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([1, 4, 9])
    # returns 98
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([1, 3, 5, 7])
    # returns 84
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([1.4, 4.2, 0])
    # returns 29
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([-2.4, 1, 1])
    # returns 6
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([1, 2, 3, 4, 5])
    # returns 90
    # 2022-10-13 14:44:13,553 - 
    # sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # returns 527
    
    n = len(lst)
    result = 0
    for i in range(n):
        result += (lst[i]**2)
    return round(result, n)
    
