def smallest_change(arr):
    # initialize the result to the length of the array
    result = len(arr)

    # Loop through the array backwards and count changing elements in loop.
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] != arr[i - 1]:
            result = min(result, 2)
        elif i != 0 and arr[i] == arr[i - 1] and arr[i] != arr[i + 1]:
            result = min(result, 1)

    return result