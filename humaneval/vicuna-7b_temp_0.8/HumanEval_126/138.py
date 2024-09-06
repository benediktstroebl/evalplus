
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
    if len(lst) == 1:
        return True
    elif len(lst) == 2:
        return lst[0] == lst[1]
    elif len(lst) > 2:
        if any(lst.count(x) > 1 for x in lst):
            return False
        return True

lst = [1, 2, 3, 4, 5]
print(is_sorted(lst))  # True

lst = [1, 2, 3, 4, 5, 6]
print(is_sorted(lst))  # True

lst = [1, 3, 2, 4, 5, 6, 7]
print(is_sorted(lst))  # True

lst = [1, 2, 3, 4, 5, 6, 7]
print(is_sorted(lst))  # True

lst = [1, 2, 2, 3, 3, 4]
print(is_sorted(lst))  # True

lst = [1, 2, 2, 2, 3, 4]
print(is_sorted(lst))  # False