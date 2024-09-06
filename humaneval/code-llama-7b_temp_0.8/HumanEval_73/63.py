
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
    n = len(arr)
    # map each element to its next (modulo the length of the list)
    next = [arr[i - 1] % n for i in range(1, len(arr))] + [0]

    # store the minimum element at each index
    min_value = [None] * n
    min_value[-1] = arr[-1]
    for i in reversed(range(len(arr) - 1)):
        min_value[i] = min(arr[i], min_value[i + 1])

    # calculate the palindrome value
    p = [
        min_value[i] if arr[i] != arr[i - 1] else arr[i]
        for i in range(len(arr) - 1)
    ] + [arr[-1]]

    # the result is the sum of the differences between the actual array and the palindrome
    return sum([abs(a - b) for a, b in zip(arr, p)])
