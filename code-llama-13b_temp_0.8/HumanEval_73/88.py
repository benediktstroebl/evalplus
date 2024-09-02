
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
    length = len(arr)
    if length == 0:
        return 0
    if length == 1:
        return 0

    # O(n)
    odd_numbers = []
    for i in range(length):
        if arr[i] % 2 != 0:
            odd_numbers.append(i)
    odd_numbers_len = len(odd_numbers)

    if odd_numbers_len == 0:
        return 0
    if odd_numbers_len == 1:
        return 1

    if (arr[0] + 1) % 2 == 0:
        odd_numbers.insert(0, -1)
    if (arr[length - 1] + 1) % 2 == 0:
        odd_numbers.append(length)

    min_changes = length + 1
    for i in range(len(odd_numbers) - 1):
        a = odd_numbers[i]
        b = odd_numbers[i + 1]
        min_changes = min(min_changes, (b - a) // 2)
    return min_changes
