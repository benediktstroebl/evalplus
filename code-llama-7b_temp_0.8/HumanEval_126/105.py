
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

    # first check if list has more than 1 duplicate of the same number
    for idx in range(len(lst)-1):
        if lst[idx] == lst[idx+1]:
            return False

    # create empty list to hold values of next index
    next_lst = []
    for num in lst:
        if num <= lst[len(lst)-2]:
            next_lst.append(lst[lst.index(num)+1])
            next_lst = list(set(next_lst))
        elif num > lst[len(lst)-2]:
            break

    # if length of next_lst is less than length of lst, return False
    if len(next_lst) < len(lst):
        return False
    # if length of next_lst is greater than or equal to length of lst, return True
    elif len(next_lst) >= len(lst):
        return True
