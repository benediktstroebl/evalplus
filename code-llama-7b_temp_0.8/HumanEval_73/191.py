
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
    # write your code here
    len_arr = len(arr)
    num_of_odd_len = 0
    if len_arr % 2 == 1:
        num_of_odd_len = 1
    start_ind = 0
    end_ind = len_arr - 1
    len_half = len_arr // 2
    # First calculate the total number of mismatched chars in the middle
    total_num_of_mismatched_char_in_middle = 0
    for i in range(start_ind, end_ind):
        if arr[i] != arr[end_ind - i - 1]:
            total_num_of_mismatched_char_in_middle += 1
    if total_num_of_mismatched_char_in_middle == 0:
        return 0
    # Second find the odd element that can be swapped to make the array palindromic
    odd_element_idx = -1
    for i in range(start_ind, end_ind):
        if arr[i] != arr[end_ind - i - 1]:
            odd_element_idx = i
            break
    # Third find the closest mismatched element to odd_element_idx
    min_diff_idx = -1
    min_diff = len_arr
    for i in range(odd_element_idx, end_ind):
        if arr[i] != arr[end_ind - i - 1]:
            diff = i - odd_element_idx
            if diff < min_diff:
                min_diff = diff
                min_diff_idx = i
    return min_diff
