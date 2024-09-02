
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
    min_len = len(arr)
    if len(arr) < 2:
        return 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                min_len = min(min_len, abs(i - j))

    return (len(arr) - min_len) // 2
