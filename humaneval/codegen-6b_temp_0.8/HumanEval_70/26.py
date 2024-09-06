
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
    if not lst: return []
    # res = [lst[0]]
    # for i in xrange(1, len(lst)):
    #     res.append(lst[i - 1] if lst[i] > lst[i - 1] else lst[i])
    # return res
    map_lst = {}
    for i, value in enumerate(lst):
        if value not in map_lst: map_lst[value] = [i]
        else: map_lst[value].append(i)
    for key, value in map_lst.items():
        map_lst[key] = [lst[i] for i in reversed(sorted(value))]
    # res = [map_lst[min(map_lst.keys())]]
    # for i in xrange(1, len(lst)):
    #     res.append(min(map_lst.keys()) if lst[i] > min(map_lst.keys()) else max(map_lst.keys()))
    # return res
    return [lst[i] for i in reversed(sorted(map_lst.keys()))]

