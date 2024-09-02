
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

    # Initialize product and sum with 1
    product, sum = 1, 1

    # Iterate over the array
    for i in arr:

        # For 0, set product to 0 and continue
        if i == 0:
            product = 0
            continue

        # Multiply the product with the absolute value of the current number
        product *= abs(i)

        # If the number is negative, multiply sum with -1
        if i < 0:
            sum *= -1

    # Return product of the absolute values of the numbers multiplied by sum
    return sum * product

