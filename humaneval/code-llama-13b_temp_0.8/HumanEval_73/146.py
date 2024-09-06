
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
    len_arr = len(arr)
    num_changes = 0
    num_items_left = len_arr
    num_middle = len_arr // 2

    while num_middle > 0:
        if arr[num_middle] != arr[len_arr - num_middle - 1]:
            num_changes += 1
            num_items_left -= 2

        num_middle -= 1

    return num_changes + num_items_left

