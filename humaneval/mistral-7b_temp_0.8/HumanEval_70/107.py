
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

    # your code here
    if not lst:
        return lst

    res = []
    while len(lst) != 1:
        max_lst = max(lst)
        res.append(max_lst)
        lst.remove(max_lst)
        min_lst = min(lst)
        res.append(min_lst)
        lst.remove(min_lst)

    res.append(lst[0])
    return res
