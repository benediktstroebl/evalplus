
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

    arr_len = len(arr)
    if arr_len == 0:
        return None

    signs_counter = {}

    for num in arr:
        if num > 0:
            signs_counter['+'] = signs_counter.get('+', 0) + 1
        elif num < 0:
            signs_counter['-'] = signs_counter.get('-', 0) + 1
        else:
            signs_counter['0'] = signs_counter.get('0', 0) + 1

    multiplier = 1
    for sign, count in signs_counter.items():
        multiplier *= (-1) ** count

    return sum(abs(num) for num in arr) * multiplier
