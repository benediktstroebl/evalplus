
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
    #if arr[0] == arr[-1]:
    #    return 0
    i = 1
    while i < len(arr)/2:
        if arr[i] != arr[-i-1]:
            break
        i += 1
    if i == len(arr)/2:
        return 0
    else:
        count = 0
        for i in range(i, len(arr)/2):
            if arr[i] != arr[-i-1]:
                count += 1
        return count + i - 1
