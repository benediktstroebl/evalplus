
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

    # if not lst:
    #     return lst
    #
    # sorted_lst = sorted(lst)
    # result = []
    # for i in range(0, len(lst), 2):
    #     result.append(sorted_lst[i])
    #     result.append(sorted_lst[i + 1])
    #
    # return result

    # another way to solve
    if not lst:
        return lst
    lst.sort()
    # lst = [5, 3, 2, 8, 6, 1, 0, 7, 4]
    result = []
    for i in range(len(lst) // 2):
        result.append(lst[i])
        result.append(lst[-1 - i])
    if len(lst) % 2 != 0:
        result.append(lst[len(lst) // 2])
    return result

