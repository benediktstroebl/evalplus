
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
    # O(n) time, O(n) space
    if len(arr) == 1:
        return 0
    arr = [str(x) for x in arr]
    # [4, 4, 5, 6, 7, 6, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1, 2, 1]
    # [4, 4, 5, 6, 7, 6, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1, 2, 1]
    arr1 = []
    for i, x in enumerate(arr):
        if i % 2 == 0:
            arr1.append(x)
        else:
            arr1.insert(0, x)
    arr2 = []
    for i, x in enumerate(arr):
        if i % 2 == 1:
            arr2.append(x)
        else:
            arr2.insert(0, x)
    # [4, 6, 7, 6, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1, 2, 1, 2, 1]
    # [4, 6, 7, 6, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1, 2, 1, 2, 1]
    # [4, 6, 7, 6, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1, 2
