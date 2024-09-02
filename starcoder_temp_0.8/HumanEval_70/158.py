
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
    # if the length of the list is less than 2, return the list
    if len(lst) < 2:
        return lst

    # else find the minimum and maximum values
    min_value = min(lst)
    max_value = max(lst)

    # then remove the minimum and maximum values from the list
    lst.remove(min_value)
    lst.remove(max_value)

    # then add minimum value to the end of the list
    lst.append(min_value)

    # then add maximum value to the front of the list
    lst.insert(0, max_value)

    # then return the list
    return lst
