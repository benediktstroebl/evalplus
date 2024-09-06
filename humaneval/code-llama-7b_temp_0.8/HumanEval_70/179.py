
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

    def find_min(lst, lower=None, upper=None):
        if len(lst) == 1:
            return lst[0]
        if upper is None:
            return find_min(lst[1:], lower, len(lst))
        elif lower is None:
            return find_min(lst[1:], upper, len(lst))
        else:
            return find_min(lst[1:], lower, upper)

    def find_max(lst, lower=None, upper=None):
        if len(lst) == 1:
            return lst[0]
        if upper is None:
            return find_max(lst[1:], lower, len(lst))
        elif lower is None:
            return find_max(lst[1:], upper, len(lst))
        else:
            return find_max(lst[1:], lower, upper)

    def strange_order(lst, lower=None, upper=None):
        if len(lst) == 1:
            return [lst[0]]
        if len(lst) == 2:
            return [lst[0], lst[1]]
        if lower is None:
            return strange_order(lst[1:], len(lst), len(lst))
        elif upper is None:
            return strange_order(lst[1:], len(lst), len(lst))
        else:
            return [find_min(lst), find_max(lst), find_min(lst[2:]), find_max(lst[2:])]

    return strange_order(lst)
