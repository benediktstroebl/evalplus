
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
    # Check that list is not empty
    if not lst:
        return False
    # Check that numbers are integers
    for i in lst:
        if not isinstance(i, int):
            return False
    # Still here? Then lst is a valid list of integers
    if lst[0] >= lst[-1]:
        return True
    # Check that there is only 1 duplicate for each number
    dis = {}
    for i in lst:
        if i in dis:
            dis[i] += 1
        else:
            dis[i] = 1
    for i in dis:
        if dis[i] > 1:
            return False
    return is_sorted(lst[1:-1])

