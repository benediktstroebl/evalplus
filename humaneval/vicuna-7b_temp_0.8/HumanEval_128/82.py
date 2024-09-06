
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

    # keep track of the sign
    sign = 1
    for num in arr:
        sign *= num

    # calculate the magnitude
    magnitude = abs(sign)

    # calculate the product of signs
    product = sign * (1 if sign == 1 else -1)

    # calculate the sum
    sum = 0
    for num in arr:
        sum += num * product

    return sum * magnitude