def can_arrange(arr):
    """Returns the largest index of an element which is not greater than or
    equal to the previous element in the given array. If no such element is
    found, return -1.

    Args:
        arr (list): A list of integers with no duplicates.

    Returns:
        int: Largest index of an element fulfilling the condition or -1.
    """
    max_idx = -1
    for idx in range(len(arr) - 1):
        if arr[idx] >= arr[idx + 1]:
            max_idx = idx
    return max_idx