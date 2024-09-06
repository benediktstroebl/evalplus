
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # your code here
    if not arr:
        return -1
    max_value = max(arr)

    if max_value * 2 > sum(arr):
        return -1

    # Approach:
    # 1) Find the largest value
    # 2) Check that the largest value is not greater than half the total sum
    # 3) Iterate through the list and the first value that is not greater than
    # or equal to the previous value is the index we're looking for.
    # 4) If the largest value is greater than the half the total sum, we know
    # there is at least one index whose value is less than the value immediately
    # preceding it.
    for i in range(len(arr)):
        if arr[i] <= arr[i - 1]:
            return i - 1
    return len(arr) - 1
