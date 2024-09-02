
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # My strategy is to iterate through the array, noting the largest value
    # and its index, then iterate again using that index to see if the
    # second loop's value is greater than the first loop's index value.
    # If it is, return the second loop's index. Otherwise, return -1.

    # We'll use this to hold the largest value and its index.
    largest = None

    # Iterate through the array, noting the largest value
    for i in range(len(arr)):
        if largest is None:
            largest = {"val": arr[i], "idx": i}
        elif arr[i] > largest["val"]:
            largest = {"val": arr[i], "idx": i}

    # If we didn't find any values, return -1
    if largest is None:
        return -1

    # If we found a largest value, iterate again using the index of that value
    # to see if we can find a value greater than it.
    for i in range(largest["idx"]):
        if arr[i] > largest["val"]:
            return i

    # If we didn't find a value greater than the largest value, return -1
    return -1

