
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
    # your solution here

    if not lst:
        return []

    if len(lst) == 1:
        return lst

    res = []
    odd_index = 1
    even_index = 0
    res.append(min(lst))
    res.append(max(lst))
    lst.remove(min(lst))
    lst.remove(max(lst))

    while lst:
        if lst:
            res.append(min(lst))
            lst.remove(min(lst))
        if lst:
            res.append(max(lst))
            lst.remove(max(lst))

    return res

