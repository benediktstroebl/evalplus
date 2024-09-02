
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
    
    lst2 = lst[:]
    lst2.sort()
    result = []
    while len(lst2) > 0:
        min_val = lst2[0]
        lst2.remove(min_val)
        result.append(min_val)
        if len(lst2) > 0:
            max_val = lst2[0]
            result.append(max_val)
            lst2.remove(max_val)
    return result

    # a = min(lst)
    # while lst:
    #     a = min(lst)
    #     lst.remove(a)
    #     result.append(a)
    #     if lst:
    #         b = max(lst)
    #         lst.remove(b)
    #         result.append(b)
    # return result

    # def _get_min(lst):
    #     a = min(lst)
    #     lst.remove(a)
    #     return a

    # return [
    #     _get_min(lst),
    #     max(lst),
    #     _get_min(lst),
    #     max(lst),
    #     _get_min(lst),
    #     max(lst),
    #     _get_min(lst),
    #     max(lst),
    #     _get_min(lst),
    #     max(lst)
    # ]
