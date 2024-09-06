
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
    # first, sort the list to ensure the number and the position are the same
    lst = sorted(lst)

    pos = 0
    size = len(lst)

    # moving through the array checking each number
    # is it higher than the number in front?
    while True:
        cur_num = lst[pos]
        if pos == size - 1:
            return True
        if lst[pos + 1] > cur_num:
            return False
        pos += 1
    # why do we return everything?
    # return False
