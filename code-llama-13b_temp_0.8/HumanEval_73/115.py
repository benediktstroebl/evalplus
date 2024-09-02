
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
    # if the array has less than 2 elements, the array is already palindromic
    if len(arr) < 2:
        return 0

    # the first and the last elements of the array must be the same
    # so we iterate over the array from the first element till the half
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            # we do not care if the elements are the same,
            # we only care how many elements are the same from the beginning and the end
            return i + len(arr) - 1 - i

    # every element of the array is the same so no elements need to be changed
    return 0

