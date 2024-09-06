
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
    if len(lst) <= 1:
        return lst
    else:
        idx = 0
        new_lst = []
        while idx < len(lst):
            min_val = min(lst[idx:])
            max_val = max(lst[idx:])
            new_lst.append(min_val)
            new_lst.append(max_val)
            idx += 1
        return new_lst

