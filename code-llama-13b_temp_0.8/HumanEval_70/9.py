
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
    # return []

    # lst.sort()
    # if not lst:
    #     return []

    # res = [lst[0]]
    # lst.remove(lst[0])
    # while lst:
    #     if res[0] == max(lst):
    #         res.insert(0, min(lst))
    #     elif res[-1] == min(lst):
    #         res.append(max(lst))

    #     lst.remove(max(lst)) if res[0] == max(lst) else lst.remove(min(lst))

    # return res

    # if not lst:
    #     return []

    # lst.sort()
    # lst.insert(0, lst.pop())
    # return lst

    lst.sort()
    lst.insert(0, lst.pop())
    return lst
