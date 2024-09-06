
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

    # lst = sorted(lst)
    # out = []
    #
    # for x in range(0, len(lst), 2):
    #     out.append(lst[x])
    #     out.append(lst[-(x+1)])
    #
    # return out

    lst = sorted(lst)
    return lst[::2] + lst[-2::-2]
