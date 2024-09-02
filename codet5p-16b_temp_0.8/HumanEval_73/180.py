
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    if len(arr) < 2: return 0
    
    pal = []
    for i in range(len(arr)):
        for j in range(len(arr)-1, -1, -1):
            pal.append(arr[i] ^ arr[j])
    
    changes = 0
    for i in range(len(pal)):
        if pal[i]!= 0:
            changes += 1
    return changes

