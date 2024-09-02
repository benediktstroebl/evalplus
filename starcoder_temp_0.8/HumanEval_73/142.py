
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
    # we need to find the number of inversions
    invs = 0
    for i, n in enumerate(arr):
        for j in range(i + 1, len(arr)):
            if arr[j] < n:
                invs += 1

    # we need to subtract the number of inversions from the middle of the array
    return len(arr) - invs // 2
