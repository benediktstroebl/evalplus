
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
    lst = lst[:]
    if not len(lst):
        return []
    out = [0] * len(lst)

    # figure out which value is the smallest
    min_value = min(lst)

    # grab all the values that are less than this value
    less_than_min = [x for x in lst if x < min_value]

    # figure out which value is the largest
    max_value = max(lst)

    # grab all the values that are not less than this value
    greater_than_max = [x for x in lst if x > max_value]

    # add these to the correct positions
    for x in range(len(less_than_min)):
        out[x] = less_than_min[x]

    for x in range(len(greater_than_max)):
        out[x + len(less_than_min)] = greater_than_max[x]
    return out
