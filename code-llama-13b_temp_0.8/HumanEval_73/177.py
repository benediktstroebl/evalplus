
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

    if not arr:
        return 0
    len_arr = len(arr)
    half_len = int(len_arr / 2)
    # print(half_len)
    if len_arr == 1:
        return 0
    elif len_arr == 2:
        return 0 if arr[0] == arr[1] else 1
    else:
        mid_idx = half_len if len_arr % 2 == 0 else half_len + 1
        # print(mid_idx)
        is_odd_len = len_arr % 2
        mid_left = mid_idx - 1
        mid_right = mid_idx + 1 if is_odd_len else mid_idx
        # print(mid_left, mid_right)
        # print(arr[mid_left], arr[mid_right])

        # print("mid_left: ", mid_left)
        if arr[mid_left] == arr[mid_right]:
            return smallest_change(arr[0:mid_left] + arr[mid_right:])
        else:
            return 1 + smallest_change(arr[0:mid_left] + arr[mid_right:])

