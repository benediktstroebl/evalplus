
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
    undo = []
    for each in arr:
        undo.append(each)

    #print(undo)
    changes = 0
    for i, each in enumerate(undo):
        changes += 1
        if undo[i] != each:
            undo[i] = each ^ 1
            undo[i] ^= undo[i]
    return changes


