
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
    m = n // 2
    arr2 = arr[:m][::-1]
    for i in range(m):
        if arr[i] != arr2[i]:
            arr[i] = arr2[i]
            arr[n - i - 1] = arr2[i]
            break
    return sum(arr[:m] != arr2[:m])
