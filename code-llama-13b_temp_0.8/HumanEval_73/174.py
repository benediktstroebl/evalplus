
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

    if not arr:
        return 0

    n = len(arr)
    half = n // 2

    odd = n % 2

    i = 0
    j = half

    count = 0
    while i < half and j < n:

        if arr[i] != arr[j]:
            count += 1
            # if count > half:
            #     return -1

        i += 1
        j += 1 if odd else -1

    return count

