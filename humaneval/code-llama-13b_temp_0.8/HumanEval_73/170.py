
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

    arr = sorted(arr)

    # the first element needs to be the same as the last element
    if arr[0] != arr[-1]:
        return 2

    odd_length = 0
    even_length = 0
    middle = len(arr) // 2

    for i, v in enumerate(arr[:middle]):
        if arr[-i - 1] == v:
            continue
        if i % 2 == 0:
            even_length += 1
        else:
            odd_length += 1

    return min(even_length, odd_length)

