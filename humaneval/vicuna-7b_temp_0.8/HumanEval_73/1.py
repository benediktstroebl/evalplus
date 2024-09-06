
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
    n = len(arr)
    min_change = float('inf')
    min_change_list = [0] * n

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    if arr[i] != arr[j] or arr[i] != arr[k] or arr[j] != arr[l] or arr[k] != arr[l]:
                        min_change_list[i] = min(min_change_list[i], min_change_list[j])
                        min_change_list[j] = min(min_change_list[j], min_change_list[k])
                        min_change_list[k] = min(min_change_list[k], min_change_list[l])
                        min_change = min(min_change, min_change_list[i] + min_change_list[j] + min_change_list[k] + min_change_list[l])

    return min_change
