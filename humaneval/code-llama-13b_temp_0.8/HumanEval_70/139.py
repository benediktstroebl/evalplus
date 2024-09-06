
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

    if lst == []:
        return []
    elif lst == [1]:
        return lst
    else:
        lst_min = min(lst)
        lst_max = max(lst)
        res = [lst_min]

        while lst:
            if lst_min in lst:
                lst.remove(lst_min)
            if lst_max in lst:
                lst.remove(lst_max)
            if lst:
                res.append(lst_max)
                lst_min = min(lst)
                lst_max = max(lst)
                res.append(lst_min)
        return res
