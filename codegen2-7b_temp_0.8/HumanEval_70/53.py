
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
    if not lst:
        return lst

    smaller, larger = (lst[0], lst[0])
    for num in lst[1:]:
        if num <= smaller:
            smaller = num
        else:
            larger = num
    lst = [smaller, larger] + sorted(lst[2:])
    return lst
