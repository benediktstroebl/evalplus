
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
        return lst
    min = 0
    max = len(lst) - 1
    lst_ordered = []
    while len(lst) > 1:
        lst_ordered.append(min(lst))
        lst.remove(min(lst))
        lst_ordered.append(max(lst))
        lst.remove(max(lst))
        max -= 1
        min += 1
    lst_ordered.append(lst[0])
    return lst_ordered
