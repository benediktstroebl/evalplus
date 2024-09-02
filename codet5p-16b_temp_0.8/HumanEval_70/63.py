
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

    minimum = min(lst)
    maximum = max(lst)
    print(minimum, maximum)
    print(lst)
    result = []
    while len(lst) > 0:
        result.append(maximum)
        result.append(minimum)
        lst.remove(minimum)
        lst.remove(maximum)
        minimum = min(lst)
        maximum = max(lst)
    return result

