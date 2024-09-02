
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
    else:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] != arr[l] or arr[mid] != arr[r]:
                return mid
            elif arr[l] > arr[mid]:
                arr[l], arr[mid] = arr[mid], arr[l]
                l += 1
            else:
                arr[mid], arr[r] = arr[r], arr[mid]
                r -= 1
        return l + 1
