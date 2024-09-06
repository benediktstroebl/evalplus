
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
    min_count = float("inf")
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count < min_count:
            min_count = count
    return min_
