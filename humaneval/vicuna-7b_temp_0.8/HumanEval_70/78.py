
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
    n = len(lst)
    res = []
    for i in range(n):
        if i == 0 or (i == n-1 and lst[i] > lst[i+1]):
            res.append(lst[i])
        else:
            min_val = min(lst)
            max_val = max(lst)
            res.append(min_val)
            res.append(max_val)
    return res
