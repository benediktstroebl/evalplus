
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

    if len(arr) == 0:
        return None

    sign_values = {1: 1, -1: 1, 0: 0}
    positive_signs = set()
    negative_signs = set()
    nonzero_signs = set()

    for number in arr:
        if number == 0:
            nonzero_signs.add(0)
        elif number > 0:
            positive_signs.add(1)
            negative_signs.add(0)
        else:
            negative_signs.add(-1)
            positive_signs.add(0)

    nonzero_sign = 1
    if len(nonzero_signs) == 0:
        nonzero_sign = 0
    elif len(nonzero_signs) > 1:
        return None

    positive_sign = 1
    if len(positive_signs) == 0:
        positive_sign = 0
    elif len(positive_signs) > 1:
        return None

    negative_sign = 1
    if len(negative_signs) == 0:
        negative_sign = 0
    elif len(negative_signs) > 1:
        return None

    return positive_sign * negative_sign * nonzero_sign * (sum(sign_values[x] for x in arr))

