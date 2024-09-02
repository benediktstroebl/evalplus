
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # base case: empty list
    if not lst:
        return True

    # find the first number
    n = lst[0]

    # loop through the list
    for i in range(1, len(lst)):
        # check if the current number is equal to the first number
        if lst[i] != n:
            return False

        # check if the current number is less than the first number
        if lst[i] < n:
            return False

        # move on to the next number
        n = lst[i]

    # if we reach this point, all numbers in the list are either equal to
    # or greater than the first number, and there are no duplicates, so
    # the list is sorted
    return True
