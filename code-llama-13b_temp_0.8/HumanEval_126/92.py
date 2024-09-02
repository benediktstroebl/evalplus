
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
    # pass

    # if 
    # if list has same number more than once:
    #     return false
    # else:
    #     sort the list
    #     compare list to original
    #     if true:
    #         return true
    #     else:
    #         return false

    if len(lst) == 1:
        return True
    
    if lst.count(lst[0]) > 1:
        return False

    original = lst.copy()
    lst.sort()
    return lst == original

    # lst.sort()
    # print(lst)
    # print(original)
    # print(lst == original)
    # return lst == original

