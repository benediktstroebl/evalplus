
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

    result = 0
    odd = False
    even = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd = True
            result += 1

    if not odd and even >= 1:
        return result

    if odd:
        return result + 1

    return result + even

