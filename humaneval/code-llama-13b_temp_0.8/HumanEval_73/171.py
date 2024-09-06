
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
    num_of_changes = 0
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            if l + 1 < len(arr) - 1 and arr[l] == arr[l + 1]:
                arr[l + 1] = arr[r]
                l += 1
                r -= 1
                num_of_changes += 1
            elif r - 1 > 0 and arr[r] == arr[r - 1]:
                arr[r - 1] = arr[l]
                r -= 1
                l += 1
                num_of_changes += 1
            else:
                num_of_changes += 2
        l += 1
        r -= 1
    return num_of_changes
