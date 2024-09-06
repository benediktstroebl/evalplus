
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
    #initialize the minimum to be the array length
    min_num = len(arr)
    #count the number of elements in the array that are not the same as their mirror elements
    count = 0
    for i in range(len(arr)):
        if arr[i] != arr[len(arr)-1-i]:
            count += 1

    #if all elements in the array are the same, then it's already palindromic
    if count == 0:
        return 0
    else:
        return count
