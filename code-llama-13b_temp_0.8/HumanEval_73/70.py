
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

    odd_counts = 0
    odds = {}
    evens = {}

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evens[arr[i]] = evens.get(arr[i], 0) + 1
        else:
            odds[arr[i]] = odds.get(arr[i], 0) + 1

    for value in evens.values():
        if value % 2 == 1:
            odd_counts += 1

    return (len(odds) + odd_counts) // 2

