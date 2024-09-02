
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
    # Result is the max distance between the first half and second half
    # of the array, so we can take the greater of the distances between
    # first and last elements and first and second to last.
    max_distance = max(arr[0] - arr[-1], arr[0] - arr[-2])
    for i in range(1, len(arr) // 2):
        max_distance = max(max_distance, arr[i] - arr[-i-1])

    return max_distance
