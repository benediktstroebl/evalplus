
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
    lst1 = []
    lst2 = []
    lst3 = []
    for i in lst:
        if i > max(lst):
            lst1.append(i)
        if i < min(lst):
            lst2.append(i)
        if i >= min(lst) and i <= max(lst):
            lst3.append(i)

    if min(lst) < max(lst):
        return lst1 + [max(lst)] + lst3 + lst2
    else:
        return lst2 + [min(lst)] + lst3 + lst1

