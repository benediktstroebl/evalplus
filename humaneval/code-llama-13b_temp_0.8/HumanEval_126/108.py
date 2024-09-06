
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
    # init a variable that holds our previous element
    prev = lst[0]
    # Loop through the list from the 2nd element to the last element
    # (starting at 1 because we already have the 0th element)
    for i in range(1, len(lst)):
        # check to see if the current element is less than our previous
        # if it is, we've passed the test
        if lst[i] < prev:
            return False
        # if it isn't, update our variable
        else:
            prev = lst[i]
    # if we get all the way through the loop, return True
    return True

