
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
    # Check if list is empty
    if lst == []:
        return lst
    # Find the minimum and maximum
    min_value = min(lst)
    max_value = max(lst)
    # Copy the list
    new_list = lst.copy()
    # Remove min and max from the list
    new_list.remove(min_value)
    new_list.remove(max_value)
    # Sort the new list
    new_list.sort()
    # Return list
    return [min_value] + new_list + [max_value]
