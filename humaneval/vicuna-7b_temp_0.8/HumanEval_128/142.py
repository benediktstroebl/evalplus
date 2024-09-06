
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

    sums = [0]
    for i in range(len(arr)):
        sign = arr[i]
        if sign == 1:
            sums.append(sums[-1] * 2)
        elif sign == -1:
            sums.append(-sums[-1] * 2)
        else:
            sums.append(sums[-1])

    product = [0]
    for i in range(len(sums)):
        product.append(sums[i])
    for i in range(len(product)):
        product[i] *= sign

    return sum(product)