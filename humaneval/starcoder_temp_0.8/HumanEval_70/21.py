
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
    # write your code here
    # Solution: 
    res = []
    if len(lst) == 1:
        return lst
    min_idx = lst.index(min(lst))
    res.append(lst[min_idx])
    lst.remove(lst[min_idx])
    res += strange_sort_list(lst)
    return res
