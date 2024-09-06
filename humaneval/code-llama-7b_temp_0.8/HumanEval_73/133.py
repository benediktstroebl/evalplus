
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
    # O(n) time and space
    n = len(arr)
    if n < 2:
        return 0

    even = [0 for _ in range(n // 2)]
    odd = [0 for _ in range(n // 2)]
    for i in range(n):
        if i % 2 == 0:
            even[i // 2] = arr[i]
        else:
            odd[i // 2] = arr[i]

    even.reverse()
    diff = 0
    for i in range(len(odd)):
        if odd[i] != even[i]:
            diff += 1

    return diff

