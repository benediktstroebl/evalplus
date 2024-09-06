
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

    min_changes = 999999
    for i in range(len(arr)):
        changes = 0
        for j in range(len(arr)):
            arr[j] = arr[j] - i
            changes += 1
            if len(arr) % 2 == 0:
                if arr[:len(arr)//2] == arr[len(arr)//2:][::-1]:
                    if min_changes > changes:
                        min_changes = changes
            else:
                if arr[:len(arr)//2] == arr[len(arr)//2+1:][::-1]:
                    if min_changes > changes:
                        min_changes = changes
            arr[j] = arr[j] + i

    return min_changes
