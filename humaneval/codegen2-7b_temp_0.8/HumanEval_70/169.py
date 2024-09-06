
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
        return lst
    else:
        m = min(lst)
        x = max(lst)
        i = len(lst)
        lst = [x for x in lst]
        lst[0] = m
        j = 0
        while j < i:
            lst[j + 1] = min(lst[j + 1], lst[j])
            lst[j] = max(lst[j], lst[j + 1])
            j += 1
        return lst
