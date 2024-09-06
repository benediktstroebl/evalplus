
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
    """
    1 2 3 4 3 2 2
    3 2 1 2 3 2 1
    2 3 1 2 3 2 1
    3 2 1 2 3 2 1
    2 3 1 2 3 2 1
    2 3 1 2 3 2 1
    3 1 1 1 2 3 2
    1 1 1 1 1 1 1
    """
    arrs = []
    for i, el in enumerate(arr):
        arrs.append([el+1, len(arr)-i])

    arrs.sort()
    while True:
        left = 0
        for i, el in enumerate(arrs[-1]):
            if el ==0:
                left = i
                break
        if left == 0:
            break
        arrs.pop()
    return left

