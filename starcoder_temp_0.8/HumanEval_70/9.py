
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
    if not lst:
        return []
    lst = lst.copy()
    min_el = min(lst)
    while True:
        if lst.count(min_el) == 1:
            min_ind = lst.index(min_el)
            break
        else:
            lst[lst.index(min_el)] = float('inf')
            min_el = min(lst)
    res = [min_el]
    lst.remove(min_el)
    while lst:
        res.append(max(lst))
        lst.remove(max(lst))
        res.append(min(lst))
        lst.remove(min(lst))
    return res
