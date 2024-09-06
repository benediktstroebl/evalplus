
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
    lst2 = []
    lst2.append(min(lst))
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    lst2.sort(reverse=True)
    lst2.reverse()
    return lst2
