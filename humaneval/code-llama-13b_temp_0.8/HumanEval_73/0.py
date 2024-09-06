
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

    l, r = 0, len(arr) - 1
    size = len(arr)
    count = 0

    while l < r:
        if arr[l] != arr[r]:
            count += 1
            # if size - 1 < 0, that means arr[r] is the same as arr[l]
            if size - 1 < 0:
                l += 1
                r -= 1
            elif arr[r] == arr[l - 1]:
                r -= 1
            elif arr[r] == arr[r + 1]:
                l += 1
        else:
            l += 1
            r -= 1

    return count

