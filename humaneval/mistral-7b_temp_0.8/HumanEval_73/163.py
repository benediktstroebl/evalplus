
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

    count = 0
    left = 0
    right = len(arr) - 1
    arr_l = [arr[i] for i in range(left, right + 1)]
    arr_r = [arr[i] for i in range(right, left - 1, -1)]

    while left <= right:
        if arr_l[count] == arr_r[count]:
            count += 1
        else:
            count += 1
            left = count
            right = len(arr) - count
            arr_l = [arr[i] for i in range(left, right + 1)]
            arr_r = [arr[i] for i in range(right, left - 1, -1)]

    return count

