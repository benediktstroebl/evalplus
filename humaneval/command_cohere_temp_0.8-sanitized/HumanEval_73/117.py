def smallest_change(arr):
    # Initialize the result to the maximum possible value
    result = len(arr)

    for i in range(len(arr) // 2):
        left, right = arr[i], arr[-1 - i]
        if left != right:
            # Calculate the number of inversions to flip the pair
            inversion_count = (i + 1) * (len(arr) - i - 1) // 2
            # Calculate the minimum changes required to make the array palindromic
            result = min(result, inversion_count + 1)

    return result