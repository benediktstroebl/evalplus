
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
    result = []
    if len(lst) == 0:
        return result
    lst_min = min(lst)
    lst_max = max(lst)
    lst_new = [x for x in lst if x != lst_min and x != lst_max]
    result.append(lst_min)
    result.append(lst_max)
    result.extend(strange_sort_list(lst_new))
    return result
