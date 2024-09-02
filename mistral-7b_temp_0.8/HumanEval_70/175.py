
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
    if len(lst)==0:
        return lst
    else:
        min_val=min(lst)
        max_val=max(lst)
        min_idx=lst.index(min_val)
        max_idx=lst.index(max_val)

        if min_idx<max_idx:
            return [min_val]+lst[:min_idx]+lst[max_idx+1:]+[max_val]
        else:
            return [max_val]+lst[:max_idx]+lst[min_idx+1:]+[min_val]

