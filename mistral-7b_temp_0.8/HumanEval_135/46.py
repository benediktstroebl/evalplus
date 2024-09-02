
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # return len(arr) - 1 if arr[::-1].count(arr[-1]) == 1 else -1
    # print(arr[-1])
    # print(arr[:-1])
    # if arr[-1] not in arr[:-1]:
    #     return len(arr) - 1
    # else:
    #     return -1

    # another way
    # arr.sort()
    # return arr.index(arr[-1])

    # third way
    lst = []
    for i in arr:
        lst.append(i)
    lst.reverse()
    return lst.index(lst[-1])


