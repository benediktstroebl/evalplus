
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
    n = len(arr)
    # if not array contains even number of elements we can't make palindromic
    # because we can't replace half of array
    if n % 2 != 0:
        return -1

    # mapping of elements into dictionary
    elements = {}
    for i in range(0, n):
        # check if array contains negative numbers
        if arr[i] < 0:
            return -1
        # if element already exists in dictionary we just need to update counter
        if elements.get(arr[i]):
            elements[arr[i]] += 1
        else:
            elements[arr[i]] = 1

    # counter for palindromic array
    counter = 0
    # number of elements we need to change
    half = n // 2
    # check if any element has odd counter
    for k, v in elements.items():
        # if odd number of elements we need to delete one
        if v % 2 != 0 and counter < half:
            counter += 1
        # if even number of elements we can just delete all
        elif v % 2 == 0:
            counter += v

    return counter
