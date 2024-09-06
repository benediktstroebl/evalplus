def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array has even length
    if len(arr) % 2 == 1:
        return len(arr) + 1

    # Initialize two variables to store the minimum values found in the two halves of the array
    min_left, min_right = float('inf'), float('inf')

    # Iterate through the right half of the array and initialize the left half variables
    for i in range(len(arr) // 2, len(arr)):
        min_right = min(min_right, arr[i])

    # Iterate from the left half of the array
    for i in range(len(arr) - 1, 0, -1):
        min_left = min(min_left, arr[i])

        # Calculate the minimum changes required
        cur_min = min(min_right, arr[i])
        if min_left != cur_min:
            return i + 1

        min_right = min_right if i != len(arr) - 1 else arr[i]

    return len(arr) // 2