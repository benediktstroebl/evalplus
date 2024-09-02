
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
        return lst

    num_of_list_values = len(lst)
    strange_sorted_list = []

    for i in range(1, num_of_list_values):
        strange_sorted_list.extend(sorted(lst[:i]))
        lst = lst[i:]

    strange_sorted_list.extend(sorted(lst))

    return strange_sorted_list
