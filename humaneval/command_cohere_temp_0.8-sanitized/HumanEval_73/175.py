def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required.
    """
    # Ensure the array contains only unique integers.
    arr = list(set(arr))
    # Sort the array.
    arr.sort()
    # Calculate the mid index.
    mid = len(arr) // 2
    # Calculate the number of changes required.
    if arr[0] == arr[mid]:
        return sum((x != arr[0] for x in arr[:mid])) + sum((x != arr[0] for x in arr[mid+1:]))
    else:
        return sum((x != arr[0] for x in arr))