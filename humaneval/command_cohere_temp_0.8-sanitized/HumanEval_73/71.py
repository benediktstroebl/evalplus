def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes
    """
    # Ensure the array has even length
    if len(arr) % 2 == 1:
        return len(arr) - 1

    # Calculate the midpoint of the array
    mid = len(arr) // 2

    # If the left and right halves of the array are equal, return 0
    if arr[:mid] == arr[mid:]:
        return 0

    # Count number of elements less than the midpoint in the right half of the array
    changes = sum(1 for num in arr[mid:] if num < mid)

    # If that count is greater than the midpoint, return that count
    if changes > mid:
        return changes

    # Otherwise return the minimum of changes required for the left and right halves
    return 1 + smallest_change(arr[:mid])