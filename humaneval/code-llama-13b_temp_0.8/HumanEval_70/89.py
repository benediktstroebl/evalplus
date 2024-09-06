
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]]
    else:
        min_num = min(lst)
        max_num = max(lst)
        new_list = [min_num]
        lst.remove(min_num)
        if max_num in lst:
            lst.remove(max_num)
        while lst:
            new_list.append(max_num)
            lst.remove(max_num)
            min_num = min(lst)
            new_list.append(min_num)
            lst.remove(min_num)
        return new_list

