
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
        return lst

    def strange_sort(lst):
        min_index = 0
        for i in range(1, len(lst)):
            if lst[min_index] > lst[i]:
                min_index = i
        min_value = lst.pop(min_index)
        lst.append(min_value)
        return lst

    new_lst = []
    while lst:
        new_lst = strange_sort(lst)
        lst = new_lst

    return new_lst
