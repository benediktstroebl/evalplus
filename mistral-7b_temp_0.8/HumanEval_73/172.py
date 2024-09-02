
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
    # your code here
    new_arr = []
    for i in arr:
        if i % 2 != 0:
            new_arr.append(i + 1)
        else:
            new_arr.append(i)
    if arr == new_arr:
        return 0
    return len(new_arr) - len(arr)
