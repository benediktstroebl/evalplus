
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # MAX_VAL = 1000
    # dp = [MAX_VAL] * MAX_VAL
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i] % arr[j] == 0 and i != j:
    #             dp[i] = j
    #             break
    # for i in range(len(arr) - 2, -1, -1):
    #     if dp[i] != MAX_VAL:
    #         return i
    # return -1
    last_i = None
    for i, num in enumerate(arr):
        if last_i is not None and num > arr[last_i] and num % arr[last_i] != 0:
            return i - 1
        last_i = i
    return -1

