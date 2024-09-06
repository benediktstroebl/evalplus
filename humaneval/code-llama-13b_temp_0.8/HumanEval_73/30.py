
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

    num_changes = 0
    n = len(arr)
    # Dictionary to keep track of all indices of elements
    indices = {x: [] for x in arr}
    for i, x in enumerate(arr):
        indices[x].append(i)

    # The number of values needed to make the array palindromic
    palindrome_len = n / 2
    # The number of values needed to make the array palindromic
    for x in indices:
        # If an index has more than one of that element, it is not needed
        if len(indices[x]) > 1:
            # Number of elements needed to make the array palindromic
            palindrome_len += 1
            # The number of values needed to make the array palindromic
            num_changes += len(indices[x]) - 1

    return num_changes - (palindrome_len - 1)

