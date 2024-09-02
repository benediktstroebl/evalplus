
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

    i = 0
    while i < len(lst):
        smallest_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest_index]:
                smallest_index = j
        lst[i], lst[smallest_index] = lst[smallest_index], lst[i]
        i += 1
    return lst

