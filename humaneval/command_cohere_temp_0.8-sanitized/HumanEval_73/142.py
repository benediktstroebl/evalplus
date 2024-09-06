def smallest_change(arr):
    # Initialize the result to the maximum possible value to minimize it
    result = len(arr)

    for i in range(len(arr) // 2):
        left, right = arr[i], arr[-1 - i]
        if left != right:
            # Compute the minimum number of changes needed to make the array palindromic
            result = min(result, abs(i - (len(arr) - 1 - i))) + 1

    return result