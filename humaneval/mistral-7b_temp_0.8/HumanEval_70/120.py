
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
    if lst == []:
        return lst
    # get a maximum value from the list and remove it
    max_val = lst[0]
    for i in range(len(lst)):
        if max_val < lst[i]:
            max_val = lst[i]
    lst.remove(max_val)
    # get a minimum value from the list and add it to the result
    min_val = lst[0]
    for i in range(len(lst)):
        if min_val > lst[i]:
            min_val = lst[i]
    return [min_val] + strange_sort_list(lst)
