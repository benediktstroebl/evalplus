
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
    if len(arr) == 1:
        return 0
    sum_left = 0
    sum_right = 0
    for i in range(0, len(arr) // 2):
        sum_left += arr[i]
        sum_right += arr[len(arr) - 1 - i]

    if sum_left != sum_right:
        return 0
    # num_to_change = 0
    # max_num = max(arr)
    # for i in arr:
    #     if i != max_num:
    #         num_to_change += 1
    # return num_to_change
    arr_sorted = sorted(arr)
    max_num = arr_sorted[-1]
    num_to_change = len(arr) - 1
    for i in arr:
        if i == max_num:
            continue
        num_to_change -= 1
    return num_to_change

