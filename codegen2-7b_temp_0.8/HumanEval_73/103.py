
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
    def helper(arr, left, right):
        if right == left:
            return 0

        if arr[left] == arr[right]:
            return helper(arr, left+1, right-1)

        return min(helper(arr, left+1, right), helper(arr, left, right-1)) + 1

    return helper(arr, 0, len(arr)-1
