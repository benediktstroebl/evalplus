
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

    if len(lst) <= 1:
        return lst

    min_value = min(lst)
    max_value = max(lst)
    max_value_index = lst.index(max_value)
    min_value_index = lst.index(min_value)

    if max_value_index < min_value_index:
        lst[0], lst[1] = lst[1], lst[0]
        max_value_index, min_value_index = min_value_index, max_value_index

    lst[1], lst[min_value_index] = lst[min_value_index], lst[1]
    lst[max_value_index+1:] = lst[1:max_value_index+1][::-1]

    return lst
