
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
        return []

    min_idx = 0
    min_val = lst[min_idx]

    for idx, val in enumerate(lst):
        if val < min_val:
            min_idx = idx
            min_val = val

    min_next = 0
    min_val_next = lst[min_next]

    for idx, val in enumerate(lst):
        if val < min_val_next and idx!= min_idx:
            min_next = idx
            min_val_next = val

    return [
        min_val,
        max(lst[:min_idx] + lst[min_idx+1:min_next] + lst[min_next+1:]),
        min_val_next,
        max(lst[min_next+1:])]
