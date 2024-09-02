
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
    if not lst:
        return []
    else:
        m = min(lst)
        lst = [x for x in lst if x!= m]
        x = strange_sort_list(lst)
        x.append(m)
        x += [y for y in lst if y == m]
        return x
