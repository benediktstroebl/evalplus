
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

    # Write your code here.
    count = 0

    if len(arr) == 1:
        return 0

    if arr[0] != arr[-1]:
        count += 1
        arr[0] = arr[-1]

    if arr[1] != arr[-2]:
        count += 1
        arr[1] = arr[-2]

    for i in range(2, len(arr) - 1):
        if arr[i] != arr[-i - 1]:
            count += 1
            arr[i] = arr[-i - 1]

    return count

