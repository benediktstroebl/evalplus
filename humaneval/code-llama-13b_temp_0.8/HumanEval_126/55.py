
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
    # Tests
    # print("is_sorted([5])", is_sorted([5]))
    # print("is_sorted([1, 2, 3, 4, 5])", is_sorted([1, 2, 3, 4, 5]))
    # print("is_sorted([1, 3, 2, 4, 5])", is_sorted([1, 3, 2, 4, 5]))
    # print("is_sorted([1, 2, 3, 4, 5, 6])", is_sorted([1, 2, 3, 4, 5, 6]))
    # print("is_sorted([1, 2, 3, 4, 5, 6, 7])", is_sorted([1, 2, 3, 4, 5, 6, 7]))
    # print("is_sorted([1, 3, 2, 4, 5, 6, 7])", is_sorted([1, 3, 2, 4, 5, 6, 7]))
    # print("is_sorted([1, 2, 2, 3, 3, 4])", is_sorted([1, 2, 2, 3, 3, 4]))
    # print("is_sorted([1, 2, 2, 2, 3, 4])", is_sorted([1, 2, 2, 2, 3, 4]))

    if lst == []:
        return True

    if len(lst) == 1:
        return True

    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i+1]:
            return False
        i += 1
    return True

