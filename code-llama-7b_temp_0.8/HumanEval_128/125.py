
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
    if arr == []:
        return None
    count_negative = sum([1 for num in arr if num < 0])
    count_positive = sum([1 for num in arr if num > 0])
    if count_negative == 0:
        return sum([num**2 for num in arr])
    if count_positive == 0:
        return sum([num**2 for num in arr]) * (-1)**count_negative
    else:
        return sum([num**2 for num in arr]) * (-1)**(count_positive - count_negative)

