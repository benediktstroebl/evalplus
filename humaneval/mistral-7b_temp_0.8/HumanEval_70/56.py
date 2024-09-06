
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
    if len(lst) <= 1:
        return lst

    min = lst[0]
    max = max(lst)
    mid = lst.index(max)

    return [min] + strange_sort_list(lst[mid+1:]) + [max] + strange_sort_list(lst[:mid])



