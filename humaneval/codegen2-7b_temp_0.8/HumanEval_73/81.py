
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
    pali = [0] * len(arr)
    pali[0] = arr[0]
    for i in range(1, len(arr)):
        pali[i] = min(pali[i - 1], arr[i])

    change_count = 0
    for i in range(len(arr)):
        if pali[i] > arr[i]:
            change_count += 1
    return change_count

