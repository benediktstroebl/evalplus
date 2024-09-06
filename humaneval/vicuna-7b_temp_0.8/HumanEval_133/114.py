

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
    sq = 0
    for num in lst:
        sq += num**2
    return round(np.sqrt(np.maximum(np.minimum(np.abs(sq), 1000000000)), 0))

for i in range(len(lst)):
    lst[i] = round(lst[i])

lst = [round(lst[i]) for i in range(len(lst))]
