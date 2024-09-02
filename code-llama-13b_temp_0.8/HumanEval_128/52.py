
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
    # Step 1: declare variables
    product = None
    # Step 2: check if array is empty
    if len(arr) == 0:
        return None
    # Step 3: declare variables
    positive = 0
    negative = 0
    # Step 4: loop over the list
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            negative += 1
    # Step 5: determine the product of all signs
    product = positive - negative
    # Step 6: return the product of the signs
    return product

