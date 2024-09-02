
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
    # Your code here
    if len(lst) <= 1:
        return lst
    minimum = min(lst)
    max_index = lst.index(max(lst))
    lst[max_index], lst[0] = lst[0], lst[max_index]
    minimum = lst[1:].index(min(lst[1:])) + 1
    return lst[0:1] + lst[minimum:] + lst[1:minimum]
