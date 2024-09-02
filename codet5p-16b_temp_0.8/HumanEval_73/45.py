
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

    size = len(arr)
    arr.sort()
    minimum_changes = size - 1
    
    for i in range(size):
        l, r = i, size - 1
        while l < r:
            if arr[l] + arr[r] == arr[i]:
                minimum_changes = min(minimum_changes, r - l)
                break
            elif arr[l] + arr[r] < arr[i]:
                l += 1
            else:
                r -= 1
    
    return minimum_changes
