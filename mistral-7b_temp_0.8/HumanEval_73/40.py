
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
    l = len(arr)
    if l==0: return 0
    if l==1: return 0
    if l==2: return 0
    if l==3: return 0
    if l==4: return 0
    if arr[0]==arr[l-1]:
        return 0
    elif arr[0]!=arr[l-1]:
        return l-1
    else:
        return smallest_change(arr[1:])+1
