
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Insertion Sort Algorithm
    for i in range(len(arr)):
        j = i - 1
        nxt_ele = arr[i]
        while j >= 0 and arr[j] > nxt_ele:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = nxt_ele
    print(arr)
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return i
    return -1

