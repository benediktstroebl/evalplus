def prod_signs(arr):
    # Start of the function
    result = None
    # Checking if the array is not empty
    if arr:
        # Creating two lists from the array
        magnitudes = [abs(x) for x in arr]  # Calculating magnitudes of each element
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]  # Calculating signs of each element
        # Performing operations on the two lists
        result = sum(magnitudes) * prod(signs)
    # Return the result
    return result