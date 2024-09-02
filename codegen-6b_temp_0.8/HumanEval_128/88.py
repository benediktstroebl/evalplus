
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

    # fast way to multiply all elements of array with sign
    # (shorter than num_pos * num_neg)
    # and check all elements for negative sign (negative * element)
    # and sign to see if its positive or negative by summing result
    # (sum of array elements * sign of number)
    return sum(x * (-1 if x < 0 else 1) for x in arr)

assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) == None
assert prod_signs([-1, -2, -2, -4]) == 3
assert prod_signs([-1, 2, -2, 4]) == -4
assert prod_signs([-1, -2, -2, 4]) == -3
assert prod_signs([-1, 2, -2, 4]) == -4
assert prod_signs([1, 2, -2, 4]) == -4
