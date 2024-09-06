
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # def can_arrange(arr):
    #     count = {}
    #     for i in arr:
    #         count[i] = count.get(i, 0) + 1
    #     for i in range(len(arr)):
    #         if i == 0:
    #             continue
    #         if arr[i] < arr[i-1] and count[arr[i]] > 0:
    #             count[arr[i]] -= 1
    #             return i
    #     return -1
    #
    # arr = sorted(arr)
    # if arr[1] > arr[0]:
    #     return 0
    # i = 1
    # while i < len(arr) - 1:
    #     if arr[i] < arr[i-1] and arr[i+1] < arr[i]:
    #         return i
    #     i += 1
    # return -1

    arr = sorted(arr)
    if arr[1] > arr[0]:
        return 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1] and arr[i+1] < arr[i]:
            return i
    return -1

