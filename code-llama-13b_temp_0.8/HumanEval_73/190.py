
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
    changes = 0
    left = 0
    right = size - 1

    while left < right:
        while left < right and arr[left] == arr[right]:
            left += 1
            right -= 1
        if left < right:
            if arr[left] != arr[right]:
                if left == left + 1 and arr[left] == arr[left + 1]:
                    left += 1
                    changes += 1
                elif right == right - 1 and arr[right] == arr[right - 1]:
                    right -= 1
                    changes += 1
                elif arr[left] == arr[right + 1]:
                    left += 1
                    right -= 1
                    changes += 2
            else:
                left += 1
                right -= 1
                changes += 2

    return changes

