
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

    
    from collections import Counter
    count = Counter(arr)
    if len(count) == 1:
        return 0
    
    odds = 0
    for num, count in count.items():
        if count % 2:
            odds += 1
        if odds > 1:
            return -1
    
    odds = [num for num, count in count.items() if count % 2]
    return len(arr) - len(odds)
