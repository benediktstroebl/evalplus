
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
    if len(arr) == 0:
        return 0

    even = arr.count(0)
    odd = 0
    for index in range(0, len(arr)-1):
        if arr[index] == arr[index+1]:
            odd += 1

    if len(arr)%2 == 0:
        if odd != 0:
            return even + (len(arr)//2)-odd
        else:
            return even + (len(arr)//2)
    else:
        if odd == 1:
            return even + (len(arr)//2)
        else:
            return even + (len(arr)//2) -1

