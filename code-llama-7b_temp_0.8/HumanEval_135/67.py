
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # if len(arr) == 0:
    #     return -1
    # # if len(arr) == 1:
    # #     return -1
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[i-1]:
    #         continue
    #     else:
    #         for j in range(i+1, len(arr)):
    #             if arr[j] >= arr[i-1] and arr[j] <= arr[i]:
    #                 continue
    #             else:
    #                 return i
    # return -1
    # arr_sort = sorted(arr)
    # print(arr_sort)
    # for i in range(len(arr_sort)-1):
    #     if arr_sort[i+1] <= arr_sort[i]:
    #         return i
    # return -1
    arr_sort = sorted(arr)
    print(arr_sort)
    for i in range(len(arr_sort)-1):
        if arr_sort[i] <= arr_sort[i+1]:
            return i
    return -1

