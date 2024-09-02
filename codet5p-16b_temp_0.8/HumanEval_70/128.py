
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

    lst_copy = lst.copy()
    lst_copy.sort()
    
    new_lst = []
    if not lst_copy:
        return new_lst
    min_value = lst_copy[0]
    max_value = lst_copy[-1]
    new_lst.append(min_value)
    new_lst.append(max_value)
    lst_copy.pop(0)
    lst_copy.pop(-1)

    new_lst.append(strange_sort_list(lst_copy))
    return new_lst

