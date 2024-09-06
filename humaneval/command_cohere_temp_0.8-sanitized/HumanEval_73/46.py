def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)

    # Reduce the result by 1 if consecutive elements are the same
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            result -= 1

    # Reduce the result if the first and last elements are the same
    if arr[0] == arr[-1]:
        result -= 1

    return result