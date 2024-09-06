
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Trivial solution: O(n^2)
    # max_val = arr[-1]
    # for i in range(len(arr) - 2, -1, -1):
    #     if arr[i] <= max_val:
    #         max_val = arr[i]
    #     else:
    #         return i
    # return -1

    # Better solution: O(n)
    # Create array of indices
    # Find the index of the first number not >= its index
    # If found, return the index
    # Otherwise return -1
    indices = [i for i in range(len(arr))]
    # indices = [0, 1, 2, 3, 4]
    # i = 0
    for i in range(len(indices) - 1):
        if arr[i] >= indices[i]:
            indices[i] = indices[i + 1]
    # indices = [0, 0, 0, 3, 3]
    # i = 0
    return indices[0] if arr[0] <= indices[0] else -1

