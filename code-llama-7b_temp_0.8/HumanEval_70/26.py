
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
    # pass # TODO: Implement function
    if len(lst) == 0:
        return []
    lst = sorted(lst)
    min = lst[0]
    lst.remove(min)
    lst.append(min)
    min = lst[0]
    lst.remove(min)
    lst.insert(0, min)
    return lst

