
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
    arr_len = len(arr)
    arr_dict = {}
    for i in xrange(arr_len):
        arr_dict[i] = arr[i]

    arr_dict_keys = arr_dict.keys()
    arr_dict_keys.sort()

    count = 0
    for i, key in enumerate(arr_dict_keys):
        while i - count <= arr_dict_keys[i-1]-key:
            if arr_dict[arr_dict_keys[i-count]] == arr_dict[key]:
                count += 1
            else:
                break
        if 2*count == arr_len:
            return count

