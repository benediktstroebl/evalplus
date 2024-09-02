
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

    # Keep list of remaining values to sort.
    # Start with full list.
    remaining = lst[:]

    # Keep sorted list of sorted values.
    sorted_values = []

    # Repeatedly pop maximum value from remaining values and append
    # it to sorted values list.
    while len(remaining):
        max_value = max(remaining)
        remaining.remove(max_value)
        sorted_values.append(max_value)

    # Repeatedly pop minimum value from remaining values and append
    # it to sorted values list.
    while len(remaining):
        min_value = min(remaining)
        remaining.remove(min_value)
        sorted_values.append(min_value)

    return sorted_values
