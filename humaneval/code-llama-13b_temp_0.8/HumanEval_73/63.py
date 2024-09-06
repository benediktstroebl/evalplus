
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
    # TODO: Your code here
    result = 0
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        while left < right and arr[left] == arr[right]:
            left += 1
            right -= 1
        if left < right:
            result += 1
            if arr[left] != arr[right]:
                if left > 0 and arr[left] == arr[left - 1]:
                    left -= 1
                elif right < n - 1 and arr[right] == arr[right + 1]:
                    right += 1
    return result
