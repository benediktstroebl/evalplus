

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
    #lst = [1,2,3]
    #lst = [1,4,9]
    #lst = [1,3,5,7]
    #lst = [1.4,4.2,0]
    #lst = [-2.4,1,1]

    new_lst = [round(num) for num in lst]
    sum_lst = sum(num**2 for num in new_lst)
    return sum_lst
