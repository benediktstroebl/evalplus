
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
    if arr == arr[::-1]:
        return 0
    else:
        if arr == sorted(arr):
            return 1
        else:
            return 2


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 4, 3, 2, 5]) == 2
assert smallest_change([4, 2, 5, 7, 9, 6]) == 4
assert smallest_change([8, 6, 0, 1, 6, 1, 1, 6]) == 3
assert smallest_change([5, 5, 1]) == 0
assert smallest_change([6,5,6,5,3,2,2,3,4]) == 4
assert smallest_change([54,5,6,5,5,6,6,35,4,5,6,35,4,5]) == 3


"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""
