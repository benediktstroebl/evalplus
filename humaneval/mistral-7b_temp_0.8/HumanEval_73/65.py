
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

    dict_arr = {}
    for i in range(0, len(arr)):
        dict_arr[arr[i]] = 0
    for i in range(0, len(arr)):
        if dict_arr[arr[i]] > 1:
            dict_arr[arr[i]] -= 1
            dict_arr[arr[-i]] += 1
    return sum([abs(v) for k, v in dict_arr.items()])
