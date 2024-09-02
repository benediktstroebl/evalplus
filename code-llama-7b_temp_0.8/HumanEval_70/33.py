
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
    if not lst:
        return []

    index, list_len = 0, len(lst)
    while index < list_len:
        min_index = index
        for index in range(index + 1, list_len):
            if lst[min_index] > lst[index]:
                min_index = index
        lst[index], lst[min_index] = lst[min_index], lst[index]
        index += 1

    return lst

