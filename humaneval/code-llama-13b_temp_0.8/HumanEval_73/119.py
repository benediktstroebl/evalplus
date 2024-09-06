
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

    odds = []
    evens = []

    for i, a in enumerate(arr):
        if i % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)

    odds = sorted(odds)
    evens = sorted(evens)

    result = 0

    for i, a in enumerate(odds):
        if a != evens[i]:
            result += 2

    return result

