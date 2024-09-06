
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

    # Auxiliary function that returns the sign of a number
    def get_sign(num):
        if num > 0:
            return 1
        if num < 0:
            return -1
        else:
            return 0

    # Initialize result to 1
    result = 1

    # Iterate over the numbers in the array
    for num in arr:
        # Get the sign of the number
        sign = get_sign(num)

        # Product of all numbers in the array multiplied by their sign
        product = result * sign

        # Sum of magnitudes of numbers in the array times their product
        result += abs(num) * product

    return result
