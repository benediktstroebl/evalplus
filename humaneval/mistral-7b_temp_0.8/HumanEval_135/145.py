
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    # Start writing your code here
    print(arr)
    print(arr.sort())
    # i=0
    # for i in arr:
    #     if arr[i] <= arr[i+1]:
    #         return arr.index(i)
    # return -1
    if arr.sort()[-1] >= arr.sort()[-2]:
        return len(arr)-1
    else:
        return -1
    # return arr.sort()[-1] >= arr.sort()[-2]
    # print(arr.sort())
    # print(arr.sort()[-1] >= arr.sort()[-2])



