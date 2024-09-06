
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

    min_value = min(lst)
    max_value = max(lst)
    result = []

    while len(lst) > 0:
        result.append(min_value)
        lst = [x for x in lst if x > min_value]
        result.append(max_value)
        lst = [x for x in lst if x < max_value]
        min_value = min(lst)
        max_value = max(lst)

    return result
