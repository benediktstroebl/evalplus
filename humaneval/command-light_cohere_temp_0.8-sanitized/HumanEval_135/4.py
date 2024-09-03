def can_arrange(arr):
    """Returns the largest index of an element which is not greater than or equal to
    the element immediately preceding it. If no such element exists then return -1"""
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            return i
    return -1