
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

    # Write your code here
    arr.sort()
    leng = len(arr)
    res = 0
    while res != leng//2:
        if arr[0] != arr[leng-1]:
            res += 1
            arr.append(arr[0])
        arr.pop(0)
    return res
