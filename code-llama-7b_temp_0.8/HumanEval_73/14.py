
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
    if len(arr) < 2:
        return 0
    res = 0
    for i in range(len(arr)//2):
        left_list = arr[0:i+1]
        right_list = arr[len(arr)-i-1:]
        left_list.reverse()
        right_list.reverse()
        print(left_list, right_list)
        if left_list == right_list:
            res += 0
        else:
            res += 1
    return res

