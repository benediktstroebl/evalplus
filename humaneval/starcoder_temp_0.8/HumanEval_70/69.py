
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

    min_value = min(lst)
    max_value = max(lst)
    if min_value == max_value:
        return lst

    # First round
    i = 0
    while i < len(lst):
        if lst[i] == min_value:
            lst.remove(lst[i])
            lst.append(min_value)
        elif lst[i] == max_value:
            lst.remove(lst[i])
            lst.insert(0, max_value)
        i += 1

    # Second round
    i = 1
    while i < len(lst):
        if lst[i] == min_value:
            lst.remove(lst[i])
            lst.append(min_value)
        elif lst[i] == max_value:
            lst.remove(lst[i])
            lst.insert(0, max_value)
        i += 2

    # Third round
    i = 0
    while i < len(lst):
        if lst[i] == min_value:
            lst.remove(lst[i])
            lst.append(min_value)
        elif lst[i] == max_value:
            lst.remove(lst[i])
            lst.insert(0, max_value)
        i += 3
    return lst

