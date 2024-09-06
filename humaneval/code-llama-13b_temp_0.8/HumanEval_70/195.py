
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

    # if list is empty, return empty list
    if not lst:
        return []

    sorted_list = sorted(lst)
    result = []

    # add minimum of the sorted list
    result.append(sorted_list[0])

    # iterate through the sorted list
    for i in range(1, len(sorted_list), 2):
        result.append(sorted_list[-i])

    # add maximum of the sorted list
    if len(sorted_list) % 2 != 0:
        result.append(sorted_list[1])

    return result

