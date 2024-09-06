
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # if not arr:
    #     return -1
    # length = len(arr)
    #
    # for i in range(length - 1):
    #     if arr[i] >= arr[i+1]:
    #         return i
    # return -1

    # Wasn't as slow as I thought
    # return next((i for i, _ in enumerate(arr[:-1]) if arr[i] >= arr[i + 1]), -1)

    # This one was the fastest
    return next((i for i, _ in enumerate(arr) if arr[i] > arr[i - 1] and arr[i - 1] > arr[i - 2]), -1)

