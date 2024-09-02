
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
    if length < 3:
        return length
    def check(arr):
        if arr[0] != arr[-1]:
            return False
        if length % 2 == 0:
            left, right = 1, length - 2
        else:
            left, right = 0, length - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
    def check_reverse(arr):
        if arr[0] != arr[-1]:
            return False
        if length % 2 == 0:
            left, right = 1, length - 2
        else:
            left, right = 0, length - 1
        while left < right:
            if arr[left] != arr[length - left - 2]:
                return False
            left += 1
            right -= 1
        return True
    if check(arr):
        return 0
    if check_reverse(arr):
