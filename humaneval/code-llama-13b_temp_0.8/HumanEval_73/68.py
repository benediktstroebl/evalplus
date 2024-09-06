
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

    # if the array is None or empty, then return 0
    if not arr:
        return 0

    # get the middle
    middle = len(arr) // 2

    # find left & right elements to compare
    left = arr[:middle]
    right = arr[middle:][::-1]

    # find the required number of swaps
    swaps = 0
    for idx, val in enumerate(left):
        if left[idx] != right[idx]:
            swaps += 1

    return swaps

