
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
    res = 0
    forward_sum = 0
    backward_sum = 0
    for i in range(len(arr)):
        forward_sum += arr[i]
    for i in range(len(arr) - 1, -1, -1):
        backward_sum += arr[i]
    if forward_sum == backward_sum:
        return res
    elif forward_sum < backward_sum:
        return res
    else:
        return forward_sum - backward_sum
