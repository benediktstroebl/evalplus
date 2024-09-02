
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
    change_count = 0
    for index, value in enumerate(arr):
        if is_palindrome(value):
            continue
        for n in range(index + 1, len(arr)):
            if arr[n] == value - arr[index]:
                change_count += 1
                break
            if arr[n] == value + arr[index]:
                change_count += 1
                break
    return change_count

