def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array has similarities at the beginning and end for easier comparison
    if len(arr) < 2:
        return 0
    arr = sorted([x for x in arr if x != 0])
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:][::-1]
    return sum([1 for x in left if x != right[0]])