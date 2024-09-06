def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes required 
    """
    # Ensure the array has even length
    if len(arr) % 2 == 1:
        return len(arr) - 1

    # Initialize two variables to count changes required for first and second half of the array
    changes_required = [0, 0]

    # Calculate changes required for first and second half of the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # If the element at arr[i] is not the same as arr[j], add 1 to changes_required[0]
            if arr[i] != arr[j]:
                changes_required[0] += 1

        # Similarly, if the element at arr[i] is not the same as arr[0], add 1 to changes_required[1]
        if arr[i] != arr[0]:
            changes_required[1] += 1

    # Return the minimum of two changes required values
    return min(changes_required)