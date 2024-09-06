
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    # result var
    result = 0
    # iterate over arr
    for number in arr:
        # if number is positive add to result
        result += abs(number)
        # multiply result by sign of number
        result *= -1 if number < 0 else 1
    return result

