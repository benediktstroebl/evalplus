
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
    def find_min(lst):
        m = min(lst)
        return lst.index(m)
    def find_max(lst):
        m = max(lst)
        return lst.index(m)

    res = []
    while lst:
        # find min
        index = find_min(lst)
        res.append(lst[index])
        lst.pop(index)
        # find max
        index = find_max(lst)
        res.append(lst[index])
        lst.pop(index)
    return res

