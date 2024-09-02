
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
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[left] != arr[mid] and arr[mid] != arr[right]:
            return mid+1
        elif arr[left] == arr[mid] and mid < right:
            arr[mid], arr[right] = arr[right], arr[mid]
            return mid+1
        else:
            left = mid + 1
    return 1
