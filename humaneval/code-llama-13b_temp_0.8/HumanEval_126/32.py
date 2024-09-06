
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

    # 1st solution
    # lst = sorted(lst)
    # lst1 = [x for i, x in enumerate(lst) if lst.index(x) != i]
    # return lst == lst1

    # 2nd solution
    for idx, i in enumerate(lst):
        if idx < len(lst) - 1:
            if i > lst[idx+1]:
                return False
        else:
            return True

    # 3rd solution
    # return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
