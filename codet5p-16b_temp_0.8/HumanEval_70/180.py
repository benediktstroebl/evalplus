
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

    result = []
    min_val, max_val = min(lst), max(lst)
    lst_len = len(lst)

    for i in range(lst_len):
        result.append(min_val)
        min_val = max_val
        max_val = max(lst[:lst_len - i])
        lst = lst[lst_len - i:]

    return result + lst
