
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

    strange_order = []

    for i in range(len(lst)):
        min_value = min(lst)
        strange_order.append(min_value)
        lst.remove(min_value)
        
        max_value = max(lst)
        strange_order.append(max_value)
        lst.remove(max_value)

    return strange_order

