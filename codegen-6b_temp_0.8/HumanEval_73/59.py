
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
    start = 0
    end = len(arr)-1
    result = 0

    while start <= end:
        if arr[start] == arr[end]:
            start += 1
        elif abs(arr[start] - arr[end]) > result:
            result = abs(arr[start] - arr[end])
        else:
            if arr[start+1] == arr[end]:
                start += 2
            elif arr[start] == arr[end-1]:
                end -= 2
            else:
                start += 1
                end -= 1

    return result

