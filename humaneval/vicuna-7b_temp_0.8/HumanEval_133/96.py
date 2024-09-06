

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
    # this is a recursive function
    # we are using the principle of divide and conquer
    # we are dividing the list into 2 parts
    # finding the sum of squared values of the left part
    # recursively
    if not lst:
        return 0
    mid = len(lst) // 2
    left = sum_squares(lst[:mid])
    right = sum_squares(lst[mid:])
    return left + right

lst = [1,2,3]
result = sum_squares(lst)
