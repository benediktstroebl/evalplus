
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
    elif len(lst) == 1:
        return lst
    else:
        new_lst = []
        min_num = min(lst)
        max_num = max(lst)
        for i in range(len(lst)):
            if i % 2 == 0:
                new_lst.append(min_num)
            else:
                new_lst.append(max_num)
        return new_lst
