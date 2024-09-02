
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
    # Your code here
    is_sorted_list = True
    duplicate_list = []
    lst_len = len(lst)
    for i in range(lst_len-1):
        if lst[i] > lst[i+1]:
            is_sorted_list = False
        elif lst[i] == lst[i+1]:
            if lst[i] not in duplicate_list:
                duplicate_list.append(lst[i])
    if len(duplicate_list) > 0:
        return False
    else:
        return is_sorted_list

