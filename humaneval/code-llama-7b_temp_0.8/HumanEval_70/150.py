
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

    # Step 1: 
    # check if the list is empty
    # if so, return an empty list
    if not lst:
        return []

    # Step 2:
    # check if list contains only one element
    # if so, return the list
    if len(lst) == 1:
        return lst

    # Step 3:
    # check if list contains more than one element
    # if so, create a copy of the original list
    lst_copy = lst.copy()

    # Step 4:
    # initialize a new empty list
    lst_sorted = []

    # Step 5:
    # find the min and max values in the list
    min_val = min(lst_copy)
    max_val = max(lst_copy)

    # Step 6:
    # add the min and max values to the new list
    lst_sorted.append(min_val)
    lst_sorted.append(max_val)

    # Step 7:
    # remove the min and max values from the original list
    lst_copy.remove(min_val)
    lst_copy.remove(max_val)

    # Step 8:
    # find the new min and max values in the new list
    # repeat until the list is empty
    while lst_copy:
        min_val = min(lst_copy)
        max_val = max(lst_copy)
        lst_sorted.append(min_val)
        lst_sorted.append(max_val)
        lst_copy.remove(min_val)
        lst_copy.remove(max_val)

    return lst_sorted
