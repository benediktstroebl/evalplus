
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
    result = [min_value]
    lst = [el for el in lst if el!= max_value and el!= min_value]
    lst = sorted(lst)
    while lst:
        result.append(lst.pop())
        result.append(min_value)
    result = result[:-1]
    while result[-1] == min_value:
        result = result[:-1]
    return result
