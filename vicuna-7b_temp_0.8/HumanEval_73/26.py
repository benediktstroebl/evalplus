
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
    m,n = len(arr),len(arr)//2
    min_num = 1
    for i in range(m):
        for j in range(n):
            if arr[i] != arr[j+n]:
                min_num = min(min_num, n)
                arr[i] = arr[j]
                arr[j+n] = arr[i]
    return min_num
