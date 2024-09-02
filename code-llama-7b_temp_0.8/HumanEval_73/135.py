
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
    result = 0
    for index, _ in enumerate(arr):
        if index % 2 == 0:
            continue
        left = index - 1
        right = index + 1
        while right < len(arr) and arr[index] != arr[right]:
            right += 1
        while left >= 0 and arr[index] != arr[left]:
            left -= 1
        result += max(right - left - 1, 0)
    return result
