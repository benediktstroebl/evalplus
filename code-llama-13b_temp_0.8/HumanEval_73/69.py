
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

    # First I need to determine the number of left and right values in the array
    # I need to create a dict to hold this info
    lr = dict()
    for i in arr:
        if i in lr:
            lr[i] += 1
        else:
            lr[i] = 1

    # now I need to get the number of odd values, this will be the answer
    odds = 0
    for i in lr:
        if lr[i] % 2 == 1:
            odds += 1

    # If all values are even, the answer is 0
    if odds == 0:
        return 0
    else:
        # If only one odd value, the answer is the number of odd values - 1
        if len(lr) == odds:
            return odds - 1
        else:
            # If there is one odd value and the rest are even, the answer is 1
            if odds == 1:
                return 1
            # If there are an even number of odd values, the answer is odds // 2
            else:
                return odds // 2

