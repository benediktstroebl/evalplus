
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

    start = min(lst)
    sorted_list = [start]
    remaining = [i for i in lst if i!= start]

    while remaining:
        end = max(remaining)
        sorted_list.append(end)
        remaining.remove(end)

        if remaining:
            start = min(remaining)
            sorted_list.append(start)
            remaining.remove(start)

    return sorted_list

