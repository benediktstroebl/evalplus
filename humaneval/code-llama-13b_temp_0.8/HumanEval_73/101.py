
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

    # count for each number in arr, 
    # and store in a dict: {1: 2, 2: 1, 3: 1, 5: 1, 4: 1, 7: 1, 9: 1, 6: 1}
    counts = {}
    for i in arr:
        counts[i] = counts.get(i, 0) + 1

    # create a dict of odd elements:
    # {1: 1, 2: 1, 3: 1, 5: 1, 4: 1, 7: 1, 9: 1, 6: 1}
    # each key has odd value, because odd numbers occur once in the list.
    odds = {}
    for i in counts:
        if counts[i] % 2:
            odds[i] = 1

    # if odds is empty, the list is palindromic
    # if len(odds) == 1, the list has only one odd number, which is the middle.
    if len(odds) == 0:
        return 0
    if len(odds) == 1:
        return 1

    # check if there is another odd number. 
    # if exists, remove the odd number from counts, and remove one from its value in odds.
    for i in odds:
        counts[i] -= 1
        if counts[i] % 2 == 0:
            del odds[i]
            break

    # if no odd number left, we can use two left and two right odd numbers to make palindromic.
    if len(odds) == 0:
        return 2

    # if we can find two odd numbers, we can use these two odd numbers to make palindromic.
    if len(odds) == 2:
        return 1

    # if we still have more than two odd numbers, we need to check if we can make palindromic
    # by using two left and two right odd numbers, and one left/right odd number.
    
