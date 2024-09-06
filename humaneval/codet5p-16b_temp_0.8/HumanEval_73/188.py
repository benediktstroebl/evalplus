
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

    pal_idx = []
    for i, val in enumerate(arr):
        if arr[i:i+2] == arr[i:i+2][::-1]:
            pal_idx.append(i)
    pal_idx.sort()
    print(pal_idx)
    count = 0
    for i, val in enumerate(pal_idx[:-1]):
        count += pal_idx[i+1] - pal_idx[i]
    return count
