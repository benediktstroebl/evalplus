
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
    if not lst:
        return []
    else:
        min_val = min(lst)
        max_val = max(lst)
        res = []
        for i in lst:
            if i == min_val:
                res.append(max_val)
                res.append(min_val)
            elif i == max_val:
                res.append(min_val)
                res.append(max_val)
            else:
                res.append(i)
        return res
