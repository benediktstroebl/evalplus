
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # This was my first thought, but it doesn't work.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         print(i)
    #         return i
    # return -1

    # Here is my second thought.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         for j in range(i):
    #             if arr[j] >= arr[i+1]:
    #                 return j
    # return -1

    # Here is my third thought.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         return i
    # return -1

    # Here is my fourth thought.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         if arr[i-1] >= arr[i+1]:
    #             return i-1
    # return -1

    # Here is my fifth thought.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         for j in range(i+1):
    #             if arr[j] >= arr[i+1]:
    #                 return j
    # return -1

    # Here is my sixth thought.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         if arr[i-1] >= arr[i+1]:
    #             return i-1
    # return -1

    # Here is my seventh thought.
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         if arr[i-1] >= arr[i+1]:
    #             return i-1
    # return -1

    # Here is my eighth thought.
    # for i in range
