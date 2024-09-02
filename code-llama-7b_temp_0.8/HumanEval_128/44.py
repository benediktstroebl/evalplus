
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

    signs = [0 if not num else num // abs(num) for num in arr]
    signs[0] = 1

    return (sum(signs) * (1 if signs[0] == -1 else -1) *
            (abs(arr[0]) * abs(arr[1])) *
            reduce(lambda x, y: x * y, [1 if sign == 1 else -1 for sign in signs]))

