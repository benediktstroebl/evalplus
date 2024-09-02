
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # we loop through the array and we create a list in which we save the
    # indexes in which the numbers are not in order
    unordered_indexes = []
    for i in range(len(arr)):
        if i > 0 and arr[i] <= arr[i-1]:
            unordered_indexes.append(i)

    if len(unordered_indexes) == 0:
        return -1

    # now we loop through the unordered indexes and we see which number is
    # the last one that is not in order
    for i in range(len(unordered_indexes)):
        if unordered_indexes[i] == len(arr) - 1:
            return unordered_indexes[i]
        else:
            return unordered_indexes[i + 1]
