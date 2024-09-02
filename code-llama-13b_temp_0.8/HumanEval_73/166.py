
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

    size = len(arr)
    is_odd = size % 2 != 0
    middle = int(size / 2)

    count = 0
    left = middle - 1
    right = middle + 1

    while left >= 0 and right < size:
        if arr[left] != arr[right]:
            count += 2
            left -= 1
            right += 1
        else:
            left -= 1
            right += 1

    if is_odd and left >= 0:
        count += 1

    return count
