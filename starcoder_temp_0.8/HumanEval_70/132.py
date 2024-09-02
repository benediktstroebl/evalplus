
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
    result = []
    if len(lst) > 0:
        sorted_list = [min(lst), max(lst)]
        lst.remove(min(lst))
        lst.remove(max(lst))
        sorted_list.extend(strange_sort_list(lst))
        result = sorted_list
    return result
