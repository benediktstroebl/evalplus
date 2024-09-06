
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
    # your code here
    # if lst == []:
    #     return []
    # lst.sort()
    # print(lst)
    # if len(lst) == 1:
    #     return lst
    # if len(lst) == 2:
    #     if lst[0] < lst[1]:
    #         return lst
    #     else:
    #         return [lst[1], lst[0]]
    # minimum = lst[0]
    # maximum = lst[-1]
    # if minimum < maximum:
    #     return [minimum] + [maximum] + strange_sort_list(lst[1:-1])
    # else:
    #     return [maximum] + [minimum] + strange_sort_list(lst[1:-1])

    if lst == []:
        return []
    lst.sort()
    print(lst)
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return [lst[0], lst[1]]
        else:
            return [lst[1], lst[0]]
    return [lst.pop(lst.index(min(lst))) , lst.pop(lst.index(max(lst))) ] + strange_sort_list(lst)
