
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
        return lst
    elif len(lst) == 2:
        return [min(lst), max(lst)]
    else:
        lst_sorted = sorted(lst)
        min_num = lst_sorted[0]
        lst_sorted.remove(min_num)
        max_num = lst_sorted.pop()
        lst_sorted.append(min_num)
        lst_sorted.insert(1, max_num)
        return lst_sorted

