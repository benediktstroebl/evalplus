def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If there are no such Administration of this array or duplicate values.

    Parameters:
    arr (array of integers)

    Returns:
        int or None if there are no duplicate values in the array, otherwise it returns -1
    """
    seen = set()
    n = len(arr)

    # find the index of the first duplicate value
    for i in range(n):
        if arr[i] in seen:
            return -1
        seen.add(arr[i])
    return i + 1