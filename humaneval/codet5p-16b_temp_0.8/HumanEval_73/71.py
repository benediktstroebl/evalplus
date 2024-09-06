
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

    def is_palindromic(arr):
        if arr == arr[::-1]:
            return True
        return False
    if is_palindromic(arr):
        return 0

    count = 0
    i = 0
    while i < len(arr):
        count += 1
        for j in range(i+1, len(arr)):
            if is_palindromic([arr[i], arr[j]]):
                return 1
        i += 1

    return count - 1
