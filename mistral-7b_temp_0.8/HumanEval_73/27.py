
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
    return 0

    # Time: O(n^2) Space: O(1)
    def recursive(arr, current_change, length):
        if length == 0:
            return current_change
        if arr[length] != arr[length - 1]:
            return min(recursive(arr, current_change + 1, length - 1) + 1,
                       recursive(arr, current_change, length - 2))
        return recursive(arr, current_change, length - 1)

    return recursive(arr, 0, len(arr) - 1)

    # Time: O(n) Space: O(n)
    def reversed_arr(arr):
        new_arr = []
        for i in range(len(arr) - 1, -1, -1):
            new_arr.append(arr[i])
        return new_arr

    def diff_arr(arr):
        new_arr = []
        for i in range(len(arr) - 1, -1, -1):
