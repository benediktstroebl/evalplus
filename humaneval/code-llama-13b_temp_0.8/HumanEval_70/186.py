
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
    new_list = []

    while len(sorted_list) > 0:
        new_list.append(sorted_list.pop(0))
        new_list.append(sorted_list.pop(-1))

    return new_list

