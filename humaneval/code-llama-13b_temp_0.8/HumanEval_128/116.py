
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
    # return None for empty arr
    if not arr:
        return None

    # set first element to multiply and sign to check
    mult = arr[0]
    sign = 1 if mult > 0 else -1 if mult < 0 else 0

    # multiply all other elements by sign and sum
    for i in arr[1:]:
        if i < 0:
            sign *= -1
        mult *= i
    return sign * mult
