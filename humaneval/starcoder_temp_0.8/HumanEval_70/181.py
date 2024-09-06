
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
    min_ = min(lst)
    max_ = max(lst)
    while max_!= min_:
        min_lst = [i for i in lst if i < max_]
        max_lst = [i for i in lst if i == max_]
        min_ = min(min_lst)
        max_ = max(max_lst)
        result = min_lst + max_lst + [max_]
        lst = [i for i in lst if i!= max_]
    return result
