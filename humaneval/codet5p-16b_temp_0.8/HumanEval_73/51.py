
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

    if len(arr) == 1:
        return 0
    elif len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1
    elif len(arr) == 3:
        if arr[0] == arr[1] or arr[0] == arr[2]:
            return 0
        elif arr[1] == arr[2]:
            return 1
        else:
            return 2
    else:
        left_pal = []
        right_pal = []
        for i in range(1, len(arr)):
            if arr[0] == arr[i]:
                left_pal.append(i)
        for i in range(len(arr)-2, -1, -1):
            if arr[len(arr) - 1] == arr[i]:
                right_pal.append(i)
        right_pal.reverse()
        if len(left_pal) == 0 and len(right_pal) == 0:
            return 0
        elif len(left_pal) == 0:
