
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

    # create an empty list to hold the sorted values
    sorted_list = []

    # create a copy of the given list to work on
    lst_copy = lst[:]

    # find the min and max of the list
    min_val = min(lst_copy)
    max_val = max(lst_copy)

    # keep track of the values that are not the min or max
    less_than_min = []
    greater_than_max = []

    # start by adding the min val to the sorted list
    sorted_list.append(min_val)

    # remove the min val from the original list
    lst_copy.remove(min_val)

    # if the list still has values
    while lst_copy:
        # if the min val is still in the list
        if min_val in lst_copy:
            # remove the min val
            lst_copy.remove(min_val)

        # if there are values left
        if lst_copy:
            # add the max val to the sorted list
            sorted_list.append(max_val)

            # remove the max val from the original list
            lst_copy.remove(max_val)

        # if the min val is not in the list anymore
        else:
            # and there are no values left
            if not lst_copy:
                # add the min val to the sorted list
                sorted_list.append(min_val)

                # and if the min val is still in the original list
                if min_val in lst_copy:
                    # remove it
                    lst_copy.remove(min_val)

        # update min and max
        min_val = min(lst_copy)
        max_val = max(lst_copy)

    return sorted_list

