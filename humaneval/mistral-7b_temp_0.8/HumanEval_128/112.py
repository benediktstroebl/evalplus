
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
    else:
        neg_magnitudes = 0
        pos_magnitudes = 0
        zero_count = 0
        for number in arr:
            if number == 0:
                zero_count += 1
            elif number < 0:
                neg_magnitudes += abs(number)
            else:
                pos_magnitudes += number
        if zero_count == len(arr):
            return 0
        else:
            return pos_magnitudes * neg_magnitudes
