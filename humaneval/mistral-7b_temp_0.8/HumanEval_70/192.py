
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

    sorted_lst = []
    min_element = min(lst)
    sorted_lst.append(min_element)
    lst.remove(min_element)
    max_element = max(lst)
    sorted_lst.append(max_element)
    lst.remove(max_element)

    while lst:
        min_element = min(lst)
        sorted_lst.append(min_element)
        lst.remove(min_element)

    return sorted_lst
