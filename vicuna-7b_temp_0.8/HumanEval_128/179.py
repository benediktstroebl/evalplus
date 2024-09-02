
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
    for i in range(len(arr)):
        if arr[i] != 0:
            product = 1
            for j in range(i, len(arr)):
                if arr[j] == -1 * arr[i]:
                    product *= -1
                elif arr[j] == -1:
                    product *= 1
                else:
                    product *= arr[j]
            result = abs(arr[i] * product)
            if result == -1 * abs(arr[i]):
                result = abs(arr[i])
            else:
                result = result if result > 0 else -result if result < 0 else 0
            return result
    return None
