
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
    # Your code here
    if len(lst) == 0:
        return []
    sorted_list = lst.copy()
    sorted_list.sort()
    strange_order = []
    min_val = sorted_list[0]
    max_val = sorted_list[-1]
    while len(sorted_list) > 0:
        strange_order.append(min_val)
        while min_val in sorted_list:
            strange_order.append(max_val)
            strange_list = max_val
            max_val = min_val
            min_val = sorted_list.pop(strange_list)
        strange_order.append(min_val)
        strange_list = min_val
        min_val = sorted_list.pop(strange_order)

    return strange_order

