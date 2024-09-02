
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
    while i < len(arr):
        if arr[i] == arr[-i-1]:
            i += 1
        else:
            break

    count = len(arr) - 1 - i
    count += 1 if i > 0 else 0
    return count

