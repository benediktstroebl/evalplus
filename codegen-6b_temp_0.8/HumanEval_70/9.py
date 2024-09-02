
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
    if lst == []:
        return []
    sort_list = []
    sort_set = set()
    minimum = min(lst)
    maximum = max(lst)
    while True:
        if not lst:
            break
        if lst[0] == minimum:
            sort_list.append(lst.pop(0))
            continue
        if lst[0] == maximum:
            sort_list.append(lst.pop(0))
            continue
        if lst[0] not in sort_set:
            sort_list.append(lst.pop(0))
            sort_set.add(lst[0])
    if lst:
        sort_list += lst
    return [sort_list, maximum]
