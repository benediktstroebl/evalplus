
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

    # start with first integer
    # if there is only one integer, return it
    # if there are more integers, add the max to list
    # if there are more integers, return the min to list
    # if there are more integers, add the max to list
    # repeat
    # return sorted list
    if len(lst) == 1:
        return lst
    else:
        max_val = max(lst)
        lst.remove(max_val)
        lst.append(max_val)
        lst.sort()
        min_val = lst.pop(0)
        lst.append(min_val)
        return lst
