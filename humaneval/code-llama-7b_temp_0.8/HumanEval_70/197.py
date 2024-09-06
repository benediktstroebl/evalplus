
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
    if len(lst) == 1 or len(lst) == 0:
        return lst

    if len(lst) == 2:
        return [min(lst), max(lst)]

    if len(lst) % 2 == 0:
        half = int(len(lst) / 2)
        return strange_sort_list(lst[:half]) + strange_sort_list(lst[half:])

    if len(lst) % 2 != 0:
        half = int(len(lst) / 2)
        return strange_sort_list(lst[:half]) + [lst[half]] + strange_sort_list(lst[half+1:])

