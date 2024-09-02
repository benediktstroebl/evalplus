
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
    # sorting the list first to find the minimum value
    lst.sort()
    # empty list
    if not lst:
        return []
    # create a new list to append the sorted elements into it
    new_lst = []
    # while list is not empty
    while lst:
        # append the minimum value of the list to the new list
        new_lst.append(lst[0])
        # remove the minimum value from the list
        lst.remove(lst[0])
        # if the list is not empty after removal
        if lst:
            # append the maximum value of the list to the new list
            new_lst.append(max(lst))
            # remove the maximum value from the list
            lst.remove(max(lst))
    # return the new list
    return new_lst

