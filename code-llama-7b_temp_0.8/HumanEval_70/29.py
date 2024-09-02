
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
    new_list = lst[:]
    new_list.sort()
    i = 0
    while i < len(new_list):
        min_value = new_list[0]
        new_list.remove(min_value)
        lst.append(min_value)
        i += 1
    return lst

