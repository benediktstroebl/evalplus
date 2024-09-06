
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
    length = len(arr)
    if length == 0 or length == 1:
        return 0

    arr.sort()

    def helper(left, right):
        if left > right:
            return 0
        if arr[left] == arr[right]:
            return helper(left+1, right-1)
        else:
            return min(arr[left] - arr[right+1],
                       arr[left-1] - arr[right],
                       helper(left+1, right),
                       helper(left, right-1)) + 1
    return helper(0, length-1)

