
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
    # s_arr = sorted(arr)
    # len_arr = len(arr)
    # min_changes = len_arr
    # i = 0
    # while i < len_arr // 2:
    #     # print(i, s_arr[i], s_arr[len_arr - 1 - i], (len_arr - 1 - i) - i)
    #     if s_arr[i] != s_arr[len_arr - 1 - i]:
    #         min_changes = min(min_changes, (len_arr - 1 - i) - i)
    #     i += 1
    # return min_changes
    s_arr = sorted(arr)
    left = 0
    right = len(s_arr) - 1
    min_changes = len(s_arr)
    while left <= right:
        if s_arr[left] != s_arr[right]:
            min_changes = min(min_changes, right - left)
        left += 1
        right -= 1
    return min_changes

