
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
    lst2 = []
    for item in lst:
        if lst2 == []:
            lst2.append(item)
        else:
            lst2.append(max(item, lst2[0]))
            lst2.insert(0, min(item, lst2[0]))
            lst2.remove(max(item, lst2[0]))
    return lst2
