
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # TODO: Write your solution here
    # if len(arr) < 2:
    #     return -1
    #
    # max_ele = max(arr)
    # min_ele = min(arr)
    #
    # if arr[-1] < max_ele:
    #     arr.append(max_ele)
    # if arr[0] > min_ele:
    #     arr.insert(0, min_ele)
    # print(arr)
    #
    # for i in range(len(arr)-2, -1, -1):
    #     if arr[i] <= arr[i+1]:
    #         continue
    #     else:
    #         for j in range(len(arr)-1, i, -1):
    #             if arr[j] >= arr[i]:
    #                 return j
    # return -1
    #
    # # TODO: Write your solution here
    # if len(arr) < 2:
    #     return -1
    #
    # for i in range(len(arr)-2, -1, -1):
    #     if arr[i] <= arr[i+1]:
    #         continue
    #     else:
    #         for j in range(len(arr)-1, i, -1):
    #             if arr[j] >= arr[i]:
    #                 return j
    # return -1


    # # TODO: Write your solution here
    # if len(arr) < 2:
    #     return -1
    #
    # arr.insert(0,min(arr))
    # arr.append(max(arr))
    # # print(arr)
    # for i in range(len(arr)-2, -1, -1):
    #     if arr[i] <= arr[i+1]:
    #         continue
    #     else:
    #         for j in range(len(arr)-1, i, -1):
    #             if arr[j] >= arr[i]:
    #                 return j
    # return -1
    #
    # # TODO: Write your solution here
    
