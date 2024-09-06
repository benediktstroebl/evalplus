
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
    # *****
    # The arr.length - 1 checks make sure that the middle of the string will always be palindromic.
    # This will only be true for even-length strings.
    # *****
    if len(arr) == 1:
        return 0

    l = 0
    r = len(arr) - 1

    while r >= l and arr[l] == arr[r]:
        l += 1
        r -= 1

    if l == r:
        return 0

    num_swaps = 0
    # *****
    # The logic in this code block is a bit confusing.
    # The arr.length - 1 checks make sure that the middle of the string will always be palindromic.
    # This will only be true for even-length strings.
    # *****
    for i in range(len(arr) - 1):
        while arr[i] == arr[r]:
            r -= 1
        num_swaps += r - i - 1

    return num
