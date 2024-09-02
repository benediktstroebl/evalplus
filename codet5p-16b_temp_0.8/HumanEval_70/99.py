
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

    sorted = strange_sort_list([x for x in lst if x > 0])

    result = []
    for n in lst:
        if n >= 0:
            result.append(n)
        else:
            result.insert(0, n)

    return result
