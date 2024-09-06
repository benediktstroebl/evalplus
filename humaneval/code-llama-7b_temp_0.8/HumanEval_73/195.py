
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
    # count the number of times a number repeats
    if not arr:
        return 0
    freq_table = {}
    for num in arr:
        if num not in freq_table:
            freq_table[num] = 0
        freq_table[num] += 1

    # find the minimum number of elements that need to be changed
    min_changes = 1e9
    for (num, freq) in freq_table.items():
        min_changes = min(min_changes, freq // 2 + freq % 2)
    return min_changes
