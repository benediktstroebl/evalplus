
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

    def strange_sort(lst):
        if len(lst) <= 1:
            return lst
        lst = sorted(lst)
        res = []
        curr = lst[0]
        res.append(curr)
        lst = lst[1:]
        curr = max(lst)
        res.append(curr)
        lst.remove(curr)
        curr = min(lst)
        res.append(curr)
        return strange_sort(res)
    return strange_sort(lst)
