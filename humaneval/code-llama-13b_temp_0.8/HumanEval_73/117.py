
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
    # Resulting count of elements to be changed
    res = 0
    # Minimum number of occurrences of any element
    min_count = float("inf")
    # Dictionary to store count of each element
    arr_dict = {}
    for el in arr:
        if el in arr_dict:
            arr_dict[el] += 1
        else:
            arr_dict[el] = 1
        min_count = min(min_count, arr_dict[el])
    # For all elements with odd count, we can only change one
    for key, val in arr_dict.items():
        if val % 2:
            res += 1
    # If number of elements to be changed is even, we can remove `min_count` number of elements
    # Else we can remove `min_count-1` elements
    return res - min_count

