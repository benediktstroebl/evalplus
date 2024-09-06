

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
    square_lst = [[lst[i]**2 for i in range(n)] for _ in range(n)]
    squared_sum = sum(square_lst)
    squared_lst = [[round(lst[i])**2 for i in range(n)] for _ in range(n)]
    round_sum = sum(squared_lst)
    return round_sum

print(sum_squares(lst))