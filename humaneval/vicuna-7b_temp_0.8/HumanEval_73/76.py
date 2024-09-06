
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
    # sort the array
    arr = sorted(arr)
    # count the number of elements in the array
    count = len(arr)
    # initialize the result to the number of elements in the array
    result = count
    for i in range(count - 1):
        # check the element at index i and its neighboring element at index i + 1
        if arr[i] != arr[i+1]:
            result = min(result, count - (i + 1))
    return result
