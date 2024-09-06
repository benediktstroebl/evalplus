
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
    l = len(arr)

    # check if array is already palindrome
    if is_palindrome(arr):
        return result

    # check if array is already sorted
    if arr == sorted(arr):
        return l // 2

    # check if array is already sorted except for one element
    if arr == sorted(arr)[:-1] + [arr[-1]]:
        return (l - 1) // 2

    # find minimum and maximum elements in the array
    minimum = min(arr)
    maximum = max(arr)

    # find the first and last element in the array
    first = arr.index(minimum)
    last = arr.index(maximum)

    # count the number of elements between the first and last element that are smaller than the first element
    if first == 0:
        first_count = 0
    else:
        first_count = arr[:first].count(minimum)

    # count the number of elements between the first and last element that are bigger than the last element
    if last == len(arr) - 1:
        last_count = 0
    else:
        last_count = arr[last + 1:].count(maximum)

    # the result is the number of elements between the first and last element that are smaller than the first element
    # and the number of elements between the first and last element that are bigger than the last element
    result = first_count + last_count

    return result

