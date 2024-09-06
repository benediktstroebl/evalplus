
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

    def is_palindromic(arr):
        return arr == arr[::-1]

    if len(arr) < 2:
        return 0

    if is_palindromic(arr):
        return 0

    # If not palindromic, then there is at least 1 change required.
    required_changes = 1

    # if first and last elems are not equal, then set first to last
    if arr[0] != arr[-1]:
        arr[0] = arr[-1]
        return 1

    # now we need to find longest palindromic suffix that is still prefix
    idx = 0
    while idx < len(arr):
        if is_palindromic(arr[idx:]):
            required_changes += (len(arr) - idx) * 2
            break
        idx += 1
    return required_changes

