
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
    arr = sorted(arr)
    length = len(arr)
    # If the array is already a palindrome, no change needed
    if arr[0] == arr[length - 1]:
        return 0

    for i in range(length):
        l = i + 1
        r = (length - 1) - i
        if arr[i] != arr[length - 1]:
            if l % 2 == 0:
                arr[l], arr[r] = arr[r], arr[l]
            else:
                arr[l], arr[r] = arr[r], arr[l]
    return length - 1
