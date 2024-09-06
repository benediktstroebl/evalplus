def smallest_change(arr):
    # initialize the result to the length of the array
    result = len(arr)

    # loop through the array and reduce result if a pair is found
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            result = min(result, 2)

    # reduce result if only one element is different from its counterpart
    for i in range(len(arr) // 2):
        if arr[i] != arr[i + 1]:
            result = min(result, 1)

    # if the result is still the length of the array, then no changes needed
    return result if result != len(arr) else 0