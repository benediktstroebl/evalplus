
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
    # Return None if array is empty
    if len(arr) == 0:
        return None

    # Count the number of positive numbers in the array
    positive = 0
    for num in arr:
        if num > 0:
            positive += 1

    # Calculate the product of the negative numbers
    negative = 1
    for num in arr:
        if num < 0:
            negative *= num

    # Calculate the product of the positive numbers
    positive_product = 1
    for num in arr:
        if num > 0:
            positive_product *= num

    # Return the sum of the magnitudes multiplied by the product of the signs
    return (positive * negative + positive_product * negative) * (positive + 1)


