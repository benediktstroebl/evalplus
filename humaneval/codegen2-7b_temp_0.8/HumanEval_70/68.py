
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
    def min_max(x):
        return max(x), min(x)

    def min_max_prev(lst):
        return min_max(lst[1:]) if len(lst) > 1 else (lst[0], lst[0])

    def strange_sort(lst, prev):
        return min_max_prev(lst[1:]) if len(lst) > 1 else (prev, lst[0])

    return sorted(lst, key=strange_sort
