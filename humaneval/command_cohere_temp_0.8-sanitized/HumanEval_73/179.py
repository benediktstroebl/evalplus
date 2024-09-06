def smallest_change(arr):
    # Initialize the result to zero or the worst case
    result = len(arr) // 2

    # Check if the array is already palindromic
    if arr == arr[::-1]:
        return 0

    for i in range(len(arr)):
        # Try swapping
        if arr[i] != arr[len(arr) - 1 - i]:
            result = min(result, 1 + smallest_change(arr[:i] + [arr[i]^1] + arr[i+1:]) )
        # If value is already correct, no changes needed
        if arr[i] == arr[len(arr) - 1 - i]:
            result = min(result, smallest_change(arr[:i] + [arr[i]] + arr[i+1:]))

    return result
arr = [1, 2, 3, 5, 4, 7, 9, 6]