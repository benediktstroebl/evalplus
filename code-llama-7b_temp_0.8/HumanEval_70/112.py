
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

    lst = sorted(lst)
    result = []
    min = lst[0]
    max = lst[len(lst)-1]
    while lst != []:
        if lst.count(min) == 1:
            result.append(min)
            lst.remove(min)
        if lst.count(max) == 1:
            result.append(max)
            lst.remove(max)
        if lst.count(min) > 1:
            result.append(min)
            lst.remove(min)
        if lst.count(max) > 1:
            result.append(max)
            lst.remove(max)
    return result

