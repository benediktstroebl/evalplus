
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # create a dictionary of index, value pairs
    dic = {}
    for i in range(len(arr)):
        dic[i] = arr[i]

    # find the largest index
    max_idx = max(dic, key=dic.get)

    # if the value of the largest index is greater than or equal to the value
    # of the index immediately preceding it, return -1
    if dic[max_idx-1] >= dic[max_idx]:
        return -1

    # return the index of the largest index
    return max_idx
