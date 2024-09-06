
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    # pass
    # print("length of arr ", len(arr))
    # print("max of arr ", max(arr))
    # print("min of arr ", min(arr))

    max_idx = -1
    if len(arr) == 2:
        if arr[1] < arr[0]:
            return 0
        return -1

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            max_idx = i - 1

    return max_idx
