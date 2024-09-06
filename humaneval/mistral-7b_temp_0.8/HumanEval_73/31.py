
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
    i = 0
    length = len(arr)
    l_index = i
    r_index = i+length-1
    while i < length:
        if arr[i] != arr[r_index]:
            return length - (r_index - l_index) + 1
        i += 1
        r_index -= 1
    return 0
