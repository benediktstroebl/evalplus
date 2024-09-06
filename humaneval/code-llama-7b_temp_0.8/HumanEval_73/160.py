
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
    if len(arr) <= 1:
        return 0
    seen = set()
    count = 0
    # Check all elements of arr in both directions
    for i in range(len(arr)):
        j = len(arr) - 1 - i
        if i == j:
            continue
        if arr[i] == arr[j]:
            continue
        if arr[i] in seen or arr[j] in seen:
            count += 1
        else:
            seen.add(arr[i])
            seen.add(arr[j])
    return count

