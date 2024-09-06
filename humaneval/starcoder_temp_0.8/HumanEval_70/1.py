
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
    # BEGIN PSEUDOCODE
    # Get the minimum value in the list
    # Make a new list containing the minimum value
    # Append the rest of the values in the list to the new list
    # Repeat step 1, 2, and 3 until the length of the list is 1
    # Return the new list
    # END PSEUDOCODE

    lst_len = len(lst)
    while lst_len > 1:
        min_value = min(lst)
        lst_min = [min_value]
        lst_other = []
        for v in lst:
            if v!= min_value:
                lst_other.append(v)
        lst = lst_min + lst_other
        lst_len -= 1
    return lst

