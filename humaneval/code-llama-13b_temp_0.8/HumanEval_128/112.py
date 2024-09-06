
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

    # SOLUTION:
    # returns 0 if empty, None otherwise.
    if len(arr) == 0:
        return 0

    # returns 1 if all elements are positive or zero, -1 if all negative or zero.
    signs = [1 if (i > 0 or i == 0) else -1 if (i < 0) else 0 for i in arr]

    # calculate the product of all signs
    prod = reduce(lambda x, y: x * y, signs)

    # returns the sum of magnitudes of integers multiplied by product of all signs
    return sum(map(abs, arr)) * prod

    # or the solution using the standard library:
    # return 0 if len(arr) == 0 else sum(map(abs, arr)) * reduce(lambda x, y: x * y, [1 if (i > 0 or i == 0) else -1 if (i < 0) else 0 for i in arr])

