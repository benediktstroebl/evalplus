
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # def find_largest_index(arr):
    #     max_index = 0
    #     max_val = 0
    #     for i, val in enumerate(arr):
    #         if val > max_val:
    #             max_val = val
    #             max_index = i
    #     return max_index

    # prev = -1
    # for i, val in enumerate(arr):
    #     if val <= prev:
    #         if val > prev:
    #             prev = val
    #         return i
    # return -1

    # for i in range(len(arr) - 2, -1, -1):
    #     if arr[i] > arr[i + 1]:
    #         return i
    # return -1

    # max_index = 0
    # max_val = 0
    # for i, val in enumerate(arr):
    #     if val > max_val:
    #         max_val = val
    #         max_index = i
    # return max_index

    # if len(arr) <= 1:
    #     return -1

    # for i in range(1, len(arr)):
    #     if arr[i] < arr[i - 1]:
    #         return i - 1
    # return len(arr) - 1

    """
    Using the idea of a "greatest index" and "lowest index" - if the element at
    the greatest index is less than or equal to the element at the lowest index,
    then we've sorted the list, so return -1. If not, we just need to keep going
    until we find an element that is less than the element just before it. We
    can then return the index of that element.
    """
    greatest_index = 0
    lowest_index = 0
    for i in range(1, len(arr)):
        if arr[greatest_index] < arr[i]:
            greatest_index = i
        if arr[lowest_index] > arr[i]:
            lowest_index = i
    if arr[gre
