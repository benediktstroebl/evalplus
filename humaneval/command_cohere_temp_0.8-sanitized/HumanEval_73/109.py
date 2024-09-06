def smallest_change(arr):
    # initialize the result to the length of the array
    result = len(arr)

    # Loop through the array and calculate the minimum number of changes required for each element
    for i in range(len(arr)):
        left, right = arr[i], arr[::-1][i]
        result = min(result, abs(left - right))

    return result