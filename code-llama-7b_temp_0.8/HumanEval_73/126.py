
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

    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    count = 0
    for k in frequency.keys():
        count += frequency[k] // 2
        if frequency[k] % 2 == 1:
            count += 1

    return count - 1
