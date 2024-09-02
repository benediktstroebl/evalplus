
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

    n = len(arr)
    odd = sum(1 for i in arr if i % 2 == 1)
    
    if odd > 1:
        return -1
    
    elif odd == 1:
        return 1
    
    else:
        return 1 - min(odd_changes(arr, i) for i in range(1, n//2+1))
