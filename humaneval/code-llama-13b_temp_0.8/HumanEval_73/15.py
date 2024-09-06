
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

    length = len(arr)
    start = 0
    end = length - 1
    change_count = 0
    while start <= end:
        if arr[start] == arr[end]:
            start += 1
            end -= 1
            continue
        else:
            left = arr[start]
            right = arr[end]
            if left < right:
                arr[start] = right
                change_count += 1
                end -= 1
            else:
                arr[end] = left
                change_count += 1
                start += 1
    return change_count
