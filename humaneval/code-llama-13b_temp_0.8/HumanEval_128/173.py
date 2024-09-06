
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
    # https://stackoverflow.com/a/13055502
    if len(arr) == 0:
        return None
    # product of signs:
    # = (n - count of zeros) for n is the number of items
    # = (len(arr) - count of zeros) for arr is the array
    # so the product of signs is calculated as
    s = len(arr) - arr.count(0)
    return sum(abs(n) * s if n else 0 for n in arr)

