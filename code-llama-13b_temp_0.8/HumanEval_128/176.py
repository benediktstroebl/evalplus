
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
    # Your code here

    if len(arr) == 0:
        return None

    total = 0
    product = 1

    for el in arr:
        if el == 0:
            product *= 1
            total += 0
        elif el < 0:
            product *= -1
            total += el
        else:
            product *= 1
            total += el

    return total * product

