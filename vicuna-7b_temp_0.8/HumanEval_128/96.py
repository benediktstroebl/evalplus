
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
    # Check if the array is empty
    if len(arr) == 0:
        return None

    # Initialize a dictionary to store the product of signs for each number
    signs_dict = {}
    for num in arr:
        if num in signs_dict:
            signs_dict[num] *= signs_dict[num]
        else:
            signs_dict[num] = 1

    # Initialize a variable to store the result
    result = 0

    # Iterate over the array and multiply the magnitudes by the product of signs
    for num in arr:
        sign = signs_dict[num]
        if sign == 1:
            result += num * sign
        elif sign == -1:
            result -= num * sign
        else:
            result += abs(num) * sign

    return result
