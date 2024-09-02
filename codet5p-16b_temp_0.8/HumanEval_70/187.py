
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

    if len(lst) == 0:
        return []

    lst = sorted(lst)
    result = []
    while len(lst) > 0:
        result.append(lst[0])
        lst = lst[1:]
        minval = min(lst)
        maxval = max(lst)
        lst = [x for x in lst if x < minval or x > maxval]
        lst = sorted(lst)
    return result
