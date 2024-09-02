
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
    n = len(lst)
    if n == 0:
        return lst
    if n == 1:
        return lst[::-1]
    first, second = 0, 1
    while second!= n:
        tmp = lst[first]
        lst[first] = lst[second]
        lst[second] = tmp
        first += 1
        second += 1
    return lst

