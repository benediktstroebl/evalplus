
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
    if len(arr) == 1:
        return 0

    odd_array = []
    for i in range(1, len(arr)):
        if arr[i] % 2 == 0:
            odd_array.append(arr[i])
    odd_array = sorted(odd_array)

    even_array = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            even_array.append(arr[i])
    even_array = sorted(even_array)

    return min(odd_array, even_array
