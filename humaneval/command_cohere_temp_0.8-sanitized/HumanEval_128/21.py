def prod_signs(arr):
    result = None
    # If the array is not empty, we proceed with the calculations.
    if arr:
        # We use a list comprehension with zipper to multiply each number by the sign of the following element.
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    # Finally, we return the calculated result.
    return result