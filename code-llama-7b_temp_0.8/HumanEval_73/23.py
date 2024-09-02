
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

    # store the sum of each character and its inverse
    s1 = 0
    s2 = 0

    for i, num in enumerate(arr):
        # for even number of digits
        if i < len(arr) / 2:
            s1 += num
        # for odd number of digits
        else:
            s2 += num

    # return the maximum value of s1 or s2
    return max(s1, s2)

