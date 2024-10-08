

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
    squared = [[0] * (n+1) for _ in range(n)]
    for i in range(1, n+1):
        squared[i-1].append(lst[i-1]**2)
    return sum([int(x)**2 for x in [sum(squared[1:])]*2])

