
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
    # convert list to list of tuples
    lst = [ tuple(x) for x in lst ]
    # sort the list of tuples in descending order
    lst = sorted(lst, reverse=True)
    # convert the list of tuples back to a list
    lst = [x[0] for x in lst]
    return lst
