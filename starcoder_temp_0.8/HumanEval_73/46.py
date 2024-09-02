
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
    left, right = 0, len(arr) - 1
    min_swaps = 0
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            if arr[left] < arr[right]:
                arr[left], arr[left + 1] = arr[left + 1], arr[left]
                min_swaps += 1
                left += 1
            elif arr[left] > arr[right]:
                arr[right], arr[right - 1] = arr[right - 1], arr[right]
                min_swaps += 1
                right -= 1
    return min_swaps

