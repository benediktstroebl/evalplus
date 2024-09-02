
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

    # boolean indicating whether the array is palindromic or not
    is_palindrome = False
    # left and right pointers
    left, right = 0, len(arr) - 1
    # number of changes to be done
    changes = 0

    while left < right and not is_palindrome:
        # is_palindrome is True if arr[left] == arr[right]
        is_palindrome = arr[left] == arr[right]
        # if not palindrome, increment changes by 2
        if not is_palindrome:
            changes += 2
        left += 1
        right -= 1

    # return the number of changes to be done
    return changes

