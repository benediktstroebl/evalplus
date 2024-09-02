
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
    smallest_len = len(arr)
    for i in range(len(arr) // 2):
        start_i, end_i = i, len(arr) - i - 1
        start_i_next, end_i_next = i, len(arr) - i - 1
        # If the first half is the same as the second half
        if arr[start_i:end_i] == arr[start_i_next:end_i_next][::-1]:
            while start_i > 0 and arr[start_i - 1] == arr[start_i]:
                start_i -= 1
            while end_i < len(arr) - 1 and arr[end_i + 1] == arr[end_i]:
                end_i += 1
            smallest_len = min(smallest_len, end_i - start_i + 1)
    return smallest_len

