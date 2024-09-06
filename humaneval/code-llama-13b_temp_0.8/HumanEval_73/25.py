
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
    if len(arr) < 2:
        return 0
    # Create hash table
    # key = array[i]
    # value = how many times this key occurs in array
    # Hash table is used to prevent duplicate values
    ht = {}
    num_unique = 0
    sum_changes = 0
    # count how many unique values there are
    for num in arr:
        if num in ht:
            ht[num] += 1
        else:
            ht[num] = 1
            num_unique += 1
    # if there are an odd number of unique values
    # then the array cannot be palindromic
    if num_unique % 2 == 1:
        return -1
    # find the middle of the array
    mid = len(arr) // 2
    # take each value and count how many differences
    # there are between that value and the middle of the array
    for num in ht:
        # if this is a palindromic number, then there is no difference between
        # the number and the middle of the array
        # if the difference is even, then we can balance the number out
        # by replacing two values
        diff = abs(num - arr[mid])
        if diff % 2 == 0:
            sum_changes += diff // 2
        # if the difference is odd, then we can balance the number out
        # by replacing one value
        else:
            sum_changes += diff
    return sum_changes

