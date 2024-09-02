
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
    try:
        if arr == []:
            return None
        elif len(arr) == 1:
            return arr[0] * arr[0]
        else:
            signs = [i % 2 for i in arr]
            return sum(arr) * prod_signs(signs)
    except TypeError:
        raise TypeError('Input should be a list of integers.')

