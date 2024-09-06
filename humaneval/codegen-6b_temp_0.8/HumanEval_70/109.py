
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
        return []
    else:
        sorted_lst = []
        min_val = min(lst[0], lst[1])
        max_val = max(lst[1], lst[2])
        for i in lst[3:]:
            if i < min_val:
                sorted_lst.append(i)
            elif i > max_val:
                sorted_lst.append(i)
            elif i > min_val and i < max_val:
                sorted_lst.append(min_val)
                sorted_lst.append(max_val)
                sorted_lst.append(i)
                sorted_lst.append(min_val)
                sorted_lst.append(max_val)
            min_val = min(min_val, i)
            max_val = max(max_val, i)
        return sorted_lst
