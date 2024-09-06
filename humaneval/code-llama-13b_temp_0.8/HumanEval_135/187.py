
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Easiest solution
    i = len(arr) - 2
    while i >= 0:
        if arr[i] > arr[i + 1]:
            break
        i -= 1
    return i

    # Clever solution
    # return max((a > b and i or -1) for i, (a, b) in enumerate(zip(arr, arr[1:])))
    # return max((a > b and i or -1) for i, (a, b) in enumerate(zip(arr, arr[1:])) if a != b)

    # More concise solution
    # return max([(a > b and i or -1) for i, (a, b) in enumerate(zip(arr, arr[1:]))])
    # return max(i for i, (a, b) in enumerate(zip(arr, arr[1:])) if a > b)

    # Cleverest solution
    # return max(range(len(arr) - 1), key=lambda i: arr[i] > arr[i + 1])
