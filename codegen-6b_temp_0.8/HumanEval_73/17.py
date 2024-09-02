
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
    start = 0
    end = len(arr)-1

    while start < end:
        if arr[start] != arr[end]:
            if arr[start+1] != arr[end]:
                return start + end - start
            end -= 1
        start +=1
    return 0


assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0

