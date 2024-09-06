
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

    first = min(lst)
    max_list = [first]
    min_list = [first]

    for value in lst:
        if value == first:
            continue
        elif value > first:
            max_list.append(value)
        else:
            min_list.append(value)

    return strange_sort_list(min_list) + max_list
