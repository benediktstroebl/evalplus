
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
    arr = list(arr)
    count = 0
    i = j = k = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
            j--
            i--
        elif arr[i] != arr[k]:
            arr[i], arr[k] = arr[k], arr[i]
            count += 1
            k--
            i--
        else:
            if count == 2:
                break
            count = 0
            i, j = j - 1, i - 1
    return count
