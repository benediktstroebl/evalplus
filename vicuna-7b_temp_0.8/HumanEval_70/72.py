
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
    # sort the list in descending order
    lst = sorted(lst, reverse=True)
    # check the last element
    if lst[-1] == 0:
        return lst[:-1]
    # if not 0, check the previous element
    elif lst[-2] == 0:
        return lst[:-2]
    # if not 0, check the previous element
    else:
        return lst[:-1]
