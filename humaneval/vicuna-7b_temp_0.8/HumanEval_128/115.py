
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
    # Check if empty
    if not arr:
        return None

    # Initialize counter for each number
    num_counter = {0: 0, 1: 0, -1: 0}

    # Loop through all numbers
    for num in arr:
        # Update counter
        if num == 0:
            num_counter[1] += 1
            num_counter[-1] += 1
        elif num == 1:
            num_counter[0] += 1
            num_counter[1] += 1
        else:
            num_counter[0] += 1
            num_counter[1] += -1
            num_counter[2] += 1

    # Calculate product of signs
    prod = num_counter[0] * (num_counter[1] * num_counter[2])

    # Calculate sum of magnitudes
    magnitude = 0
    for num in arr:
        magnitude += num

    # Calculate product of magnitudes
    prod_mag = magnitude * prod

    # Calculate final result
    result = prod_mag * (1 if magnitude > 0 else -1) * (1 if magnitude == 0 else 0)

    return result