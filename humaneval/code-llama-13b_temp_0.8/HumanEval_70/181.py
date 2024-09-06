
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
    while lst:
        if len(lst) > 1:
            minimum = min(lst)
            lst.remove(minimum)
            maximum = max(lst)
            lst.remove(maximum)
            lst.insert(0, minimum)
            lst.insert(1, maximum)
            return lst
        else:
            return lst

