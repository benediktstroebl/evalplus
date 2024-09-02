
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

    sorted_list = sorted(lst)
    strange_list = []
    while len(sorted_list) > 0:
        strange_list.append(sorted_list[0])
        sorted_list.remove(sorted_list[0])
        sorted_list = [n for n in sorted_list if n > sorted_list[0]]
    strange_list = strange_list + sorted_list
    return strange_list

