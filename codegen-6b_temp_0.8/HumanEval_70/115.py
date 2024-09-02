
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
        return []
    else:
        lst.sort()
        min_element = lst.pop(0)
        new_list = [min_element]
        for element in lst:
            if element > min_element:
                min_element = element
                new_list.append(min_element)
        new_list += lst
    return new_list
