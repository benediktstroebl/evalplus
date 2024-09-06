def smallest_change(arr):
    # initialize the variable result to store the number of changes
    result = float('inf')

    # loop through the array and calculate the minimum number of changes
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            # one change in the first i elements and one change in the last j elements
            temp = abs(arr[i] - arr[0]) + abs(arr[j] - arr[-1])
            # assign the minimum value of result and temp
            result = min(result, temp)

    # return the result
    return result