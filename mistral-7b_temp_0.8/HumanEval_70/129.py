
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
    #print(lst)
    i = 0
    while i < len(lst):
        min_val = lst[i]
        max_val = lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] < min_val:
                min_val = lst[j]
                lst[i], lst[j] = lst[j], lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] > max_val:
                max_val = lst[j]
                lst[i], lst[j] = lst[j], lst[i]
        i += 1

    return lst
