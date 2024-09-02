
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
    # check for empty lists
    if not lst:
        return []
    # make a new list with minimum value
    new_lst = [min(lst)]
    # iterate over the list
    for i in range(len(lst)):
        # remove minimum value from lst and append to new list
        new_lst.append(lst.pop(lst.index(min(lst))))
    return new_lst
