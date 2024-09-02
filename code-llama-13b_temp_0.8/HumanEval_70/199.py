
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

    # first get the lowest value from the list
    # remove that value from the list
    # add to new list
    # get the highest value from the list
    # remove that value from the list
    # add to new list

    # initialize new list to be returned
    new_list = []
    # while there are still integers in the original list
    while lst:
        # get the lowest value in the list
        lowest_val = min(lst)
        # remove the lowest value from the list
        lst.remove(lowest_val)
        # add the lowest value to the new list
        new_list.append(lowest_val)
        # get the highest value in the list
        highest_val = max(lst)
        # remove the highest value from the list
        lst.remove(highest_val)
        # add the highest value to the new list
        new_list.append(highest_val)
    # return the new list
    return new_list
