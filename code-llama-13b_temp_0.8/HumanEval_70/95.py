
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
    def sort(l, res):
        if not l:
            return res
        min_elem = min(l)
        res.append(min_elem)
        return sort(l[1:], res)
    def reverse_sort(l, res):
        if not l:
            return res
        max_elem = max(l)
        res.append(max_elem)
        return reverse_sort(l[1:], res)
    l = sorted(lst)
    res = []
    while l:
        res = sort(l, res)
        res = reverse_sort(l, res)
    return res

