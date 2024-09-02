
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
    length = len(arr)
    max_change = (length * (length + 1) // 2) // 2
    change = 0
    for i in range(max_change):
        for j in range(i + 1, length):
            if arr[j] != arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                change += 1
                break
    return change
