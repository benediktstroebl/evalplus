def prod_signs(arr):
    # Start by initializing the result to None. This is our default return value.
    result = None
    # If the input array is not empty, we proceed with the calculations.
    if arr:
        # Create two lists: 'magnitudes' to store the magnitude of each number, and 'signs' to store the signs of each number (1, -1, or 0).
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        # Calculate the final result as the sum of magnitudes multiplied by the product of signs.
        result = sum(magnitudes) * prod(signs)
    # If the input array is empty, we return None.
    return result