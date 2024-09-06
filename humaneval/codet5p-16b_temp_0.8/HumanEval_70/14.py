
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

    print(lst)
    min_value = min(lst)
    strange_list = [min_value]
    for x in lst[1:]:
        if x > min_value:
            strange_list.append(x)
            min_value = min(strange_list)
        else:
            strange_list.append(x)
    print(strange_list)
    return strange_list
