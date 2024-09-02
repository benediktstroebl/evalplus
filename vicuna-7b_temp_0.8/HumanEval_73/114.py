
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
    min_change = arr[0]
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            change = abs(arr[i] - arr[j])
            if change < min_change:
                min_change = change
    return min_change
