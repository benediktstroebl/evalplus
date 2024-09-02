
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
    else:
        min_el = min(lst)
        new_lst = []
        new_lst.append(min_el)
        for i in range(lst.count(min_el)):
            lst.remove(min_el)
        max_el = max(lst)
        new_lst.append(max_el)
        for i in range(lst.count(max_el)):
            lst.remove(max_el)
        new_lst.append(lst)
        new_lst = new_lst[0] + new_lst[1] + new_lst[2]
        return new_lst
