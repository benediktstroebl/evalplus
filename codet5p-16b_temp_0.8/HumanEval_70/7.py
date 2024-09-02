
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

    def strange_sort(lst, reverse=False):
        if len(lst) <= 1:
            return lst
        else:
            start = lst.index(min(lst))
            if reverse:
                return [lst[start]] + strange_sort(lst[:start] + lst[start+1:], True) + strange_sort(lst[start+1:], False)
            else:
                return strange_sort(lst[:start] + [lst[start]] + lst[start+1:], False) + strange_sort(lst[start+1:], True)
    return strange_sort(lst, reverse=False)

