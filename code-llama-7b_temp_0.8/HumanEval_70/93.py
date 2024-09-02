
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
    # if len(lst) == 1:
    #     return lst
    # if len(lst) == 0:
    #     return []
    # res = []
    # num = min(lst)
    # lst.remove(num)
    # res.append(num)
    # lst2 = max(lst)
    # res.append(lst2)
    # return res + strange_sort_list(lst)

    # your code here
    res = []
    if not lst:
        return res

    while lst:
        min_val = min(lst)
        max_val = max(lst)

        if len(lst) == 1:
            res.append(lst[0])
            break

        if lst.count(min_val) == 1:
            res.append(min_val)
        else:
            res.append(max_val)

        lst.remove(min_val)
        lst.remove(max_val)

    return res

