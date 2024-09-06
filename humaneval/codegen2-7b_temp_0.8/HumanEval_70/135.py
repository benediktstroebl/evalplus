
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
        return lst
    min_val = min(lst)
    strange_list = [max(lst) for _ in range(len(lst))]
    strange_list.sort(reverse=True)
    lst.sort()
    lst = [min_val] + strange_list + lst
    return lst
