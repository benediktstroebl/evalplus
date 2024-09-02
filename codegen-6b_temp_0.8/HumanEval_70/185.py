
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
    lst = sorted(lst)
    if not lst:
        return lst

    next_min = lst[0]
    ordered = [next_min]
    for i in range(1, len(lst)):
        next_val = lst[i]
        if next_val > next_min:
            ordered.append(next_val)
            next_min = min(next_min, next_val)
        elif next_val < next_min:
            ordered.append(next_min)
            next_min = max(next_min, next_val)
    ordered.append(next_min)
    return ordered

