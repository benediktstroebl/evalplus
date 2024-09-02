
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
    if lst == []:
        return lst
    max_ = max(lst)
    min_ = min(lst)
    out = [max_]
    for i in lst:
        if i != max_ and i != min_:
            out.append(min_)
            min_ = i
    return out + out[-2::-1]
