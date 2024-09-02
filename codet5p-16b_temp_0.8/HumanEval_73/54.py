
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

    if arr == arr[::-1]:
        return 0

    palindromic = {}
    for num in arr:
        if num in palindromic:
            palindromic[num] += 1
        else:
            palindromic[num] = 1

    min_changes = len(arr) - max(palindromic.values())
    for value in palindromic.values():
        if value % 2!= 0:
            min_changes += 1
    return min_changes
