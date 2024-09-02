
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
    # Use a dictionary to keep track of the values
    values = [lst[0]]
    for i in range(1, len(lst)):
        values.append(max(lst[i], values[-1]))
    for i in range(1, len(lst)):
        values[i] = min(lst[i], values[-1])
    return values