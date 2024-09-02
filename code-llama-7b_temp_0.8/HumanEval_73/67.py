
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # find largest element in array
    largest = 0
    for el in arr:
        if el > largest:
            largest = el
    # create a new array of zeros of length largest + 1
    new_arr = [0] * (largest + 1)
    # create a new array of zeros of length largest + 1
    # iterate over new arr
    for i in range(len(new_arr)):
        new_arr[i] = [0] * (largest + 1)
    # iterate over the array
    for i in range(len(arr)):
        # iterate over the array
        for j in range(len(arr)):
            # if arr[i] == arr[j] and i != j
            if arr[i] == arr[j] and i != j:
                new_arr[i][j] = 1
    # iterate over the new arr
    for i in range(len(new_arr)):
        # iterate over the new arr
        for j in range(len(new_arr[i])):
            # if new arr [i] [j] > 0
            if new_arr[i][j] > 0:
                # return largest + 1 - j
                return largest + 1 - j
    return 0

