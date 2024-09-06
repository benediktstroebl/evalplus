
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # version 1
    # result = []
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[i - 1]:
    #         result.append(i)
    # if len(result) == 0:
    #     return -1
    # else:
    #     return max(result)
    # version 2

    # result = [0]
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[i - 1]:
    #         result.append(i)
    # if len(result) == 0:
    #     return -1
    # else:
    #     return max(result)

    # version 3
    # return max(range(1, len(arr)), key=lambda i: arr[i] if arr[i] >= arr[i - 1] else -1)

    # version 4
    # return max(range(1, len(arr)), key=lambda i: arr[i] if arr[i] >= arr[i - 1] else -1)

    # version 5
    # return max(range(1, len(arr)), key=lambda i: arr[i] if arr[i] >= arr[i - 1] else -1)

    # version 6
    return max(range(1, len(arr)), key=lambda i: arr[i] if arr[i] >= arr[i - 1] else -1)


assert can_arrange([1, 2, 4, 3, 5]) == 3
assert can_arrange([1, 2, 3]) == -1
assert can_arrange([1, 2, 4, 6, 10, -1, 2, 3, 5]) == 4
assert can_arrange([1, 2, 3, 5]) == -1
assert can_arrange([1, 2, 3, 4]) == -1
assert can_arrange([1, 2, 4, 3, 5]) == 3
assert can_arrange([1, 2, 4, 3]) == -1
assert can_arrange([1, 2, 4, 3, 3]) == 3
assert can_arrange([1, 2, 3