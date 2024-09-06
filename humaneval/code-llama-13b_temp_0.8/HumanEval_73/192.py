
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

    half_l = arr[0:int(len(arr) / 2)]
    half_r = arr[int(len(arr) / 2):][::-1]
    change_count = 0

    for i in range(len(half_l)):
        if half_l[i] != half_r[i]:
            change_count += 1

    return change_count

