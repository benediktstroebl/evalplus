
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # We will use the concept of prefix sums to solve this
    # We initialize the prefix sums array
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Now that we have the prefix sums, we know that the prefix_sum[i] gives
    # the sum of all the values that are present up to the ith index
    # To figure out if we can arrange the array, we need to see if the
    # prefix_sum[i] is greater than the prefix_sum[j - 1],
    # where j > i
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if prefix_sum[j] - prefix_sum[i] >= 0:
                return i
    return -1
