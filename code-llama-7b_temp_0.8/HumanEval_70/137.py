
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
    #your code here
    if not lst:
        return lst
    # print(lst)
    # print(min(lst), max(lst))
    # if len(lst) == 1:
    #     return lst
    # if len(lst) > 1:
    #     return [min(lst)] + [max(lst[1:])] + lst[2:]
    # else:
    #     return lst
    # print(lst[0])
    # if len(lst) > 1:
    #     lst[0], lst[1] = lst[1], lst[0]
    # print(lst)
    # lst[1:] = lst[1:].sort(reverse=True)
    # print(lst)
    # lst = lst.sort(reverse=True)
    # print(lst)
    # lst = sorted(lst, reverse=True)
    # print(lst)
    # lst = sorted(lst, reverse=True)
    # print(lst)
    # lst = sorted(lst, reverse=True)
    # print(lst)
    # lst = sorted(lst, reverse=True)
    # print(lst)
    # lst = sorted(lst, reverse=True)
    # print(lst)

    return [min(lst)] + [max(lst[1:])] + lst[2:]
