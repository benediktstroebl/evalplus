
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
    if len(lst) <= 1:
        return lst
    def sort_by_min(lst):
        return sorted(lst, key=lambda x: min(lst))

    def sort_by_max(lst):
        return sorted(lst, key=lambda x: max(lst))

    return sort_by_max(sort_by_min(lst)[:]) + sort_by_min(sort_by_max(lst)[:])
