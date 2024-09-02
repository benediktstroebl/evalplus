
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

    # get a list of the sign values of the items in the array
    # where positive is represented by 1, negative by -1 and 0 for neutral
    signs = []
    for a in arr:
        signs.append(1 if a >= 0 else -1)
    print(signs)

    # calculate the product of the sign list
    product = 1
    for s in signs:
        product = product * s

    # calculate the sum of the product of the magnitude of each item
    # multiplied by the product of the signs
    sum = 0
    for a in arr:
        sum += a * product
    return sum

