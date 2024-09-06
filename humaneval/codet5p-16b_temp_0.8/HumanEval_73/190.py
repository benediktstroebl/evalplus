
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

    max_num = max(arr)
    max_len = len(str(max_num))
    changes = 0
    for i in range(1, max_len+1):
        change = i
        for n in range(max_num+1):
            if n < 10**(max_len - i):
                continue
            if arr[n - 10**(max_len - i)] == n % 10:
                change = 0
            else:
                change += 1
        changes = max(changes, change)
    return changes
