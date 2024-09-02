
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
    # Your code here
    num_odd = 0
    num_to_change = 0
    if len(arr) <= 1:
        return 0
    arr.sort()
    if arr[0] != arr[len(arr) - 1]:
        num_odd += 1
    if num_odd % 2 == 1:
        num_to_change += 1
    i = 1
    j = len(arr) - 2
    while i < j:
        if arr[i] != arr[j]:
            num_to_change += 1
        i += 1
        j -= 1
    return num_to_change

