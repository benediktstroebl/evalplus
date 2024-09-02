
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
    max_ele = max(arr)

    count_arr = [0] * (max_ele + 1)

    for i in range(n):
        count_arr[arr[i]] += 1

    res = 0
    for i in range(1, max_ele + 1):
        res += min(count_arr[i], count_arr[max_ele - i])

    return res

