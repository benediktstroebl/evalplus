
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
    if len(arr) < 2:
        return 0

    # map characters to their occurrences
    count = Counter(arr)

    # sum the number of odd occurrences
    extra = sum(count[k] % 2 for k in count)

    # if the array is already palindromic
    if extra == 0:
        return 0
    # if the array is not palindromic and has an even number of elements
    elif extra % 2 == 0:
        return extra // 2
    # otherwise, the array cannot be palindromic
    return -1

