

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
    sum_of_squares = 0
    for i in range(n):
        if i == n-1:
            lst_upper = lst[i].upper() + lst[i+1].lower()
        else:
            lst_upper = lst[i].upper()
        lst_squared = lst[i]**2
        sum_of_squares += lst_squared * lst_upper
    return round(sum_of_squares)