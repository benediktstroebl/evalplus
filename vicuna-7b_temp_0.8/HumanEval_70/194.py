
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
    # Return empty list if input list is empty
    if not lst:
        return []

    # Get minimum value
    min_val = min(lst)

    # Get maximum value
    max_val = max(lst)

    # Get all values in between
    values = [x for x in lst[1:]]

    # Start sorting
    result = []
    for value in values:
        result.append(value)
        result.append(max_val)
        result.append(min_val)

    return result