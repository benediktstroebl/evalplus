
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
    # check that the list is not empty
    if len(lst) == 0:
        return []
    # check that the list is not empty
    if len(lst) == 1:
        return lst

    # initiate an empty list
    lst_strange = []
    # while loop for an odd number of integers
    while len(lst) > 0:
        min_val = lst[0]
        max_val = lst[0]
        # find the minimum and maximum values in the list
        for num in lst:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num

        # append the minimum and maximum values to the list
        lst_strange.append(min_val)
        lst_strange.append(max_val)
        # remove the minimum and maximum values from the list
        lst.remove(min_val)
        lst.remove(max_val)

    return lst_strange

