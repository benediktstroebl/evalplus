
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

    sorted_list = []
    lst.sort(reverse=True)
    for x in range(0, len(lst), 2):
        sorted_list.append(lst[x])
    for x in range(1, len(lst), 2):
        sorted_list.append(lst[x])

    return sorted_list
