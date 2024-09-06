
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
    # sort the list
    lst = sorted(lst)

    # get the minimum value
    min_value = lst[0]

    # get the maximum of the remaining integers
    max_value = max(lst[1:])

    # get the indices of the remaining integers
    indices = [i for i, val in enumerate(lst[1:]) if val > max_value]

    # append the indices to the list
    result = [min_value]
    for index in indices:
        result.append(lst[index])

    return result
