
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

    # return sorted(lst, key=lambda x: lst[lst.index(x) % 2], reverse=True)

    # def key_func(x):
    #     return lst[lst.index(x) % 2]

    # return sorted(lst, key=key_func, reverse=True)

    # if not lst:
    #     return []

    # sorted_lst = sorted(lst)
    # sorted_min_lst = [sorted_lst[0]]
    # sorted_max_lst = sorted_lst[1:]
    # sorted_max_lst = sorted(sorted_max_lst, reverse=True)
    # return sorted_min_lst + sorted_max_lst

    # lst_len = len(lst)
    # lst_half_len = lst_len // 2
    # sorted_lst = sorted(lst)
    # sorted_min_lst = sorted_lst[:lst_half_len]
    # sorted_max_lst = sorted_lst[lst_half_len:]
    # sorted_max_lst = sorted(sorted_max_lst, reverse=True)
    # return sorted_min_lst + sorted_max_lst

    # if not lst:
    #     return []

    # lst_len = len(lst)
    # sorted_lst = sorted(lst)
    # sorted_min_lst = [sorted_lst[0]]
    # sorted_max_lst = sorted_lst[1:]
    # sorted_max_lst = sorted(sorted_max_lst, reverse=True)
    # sorted_max_lst = [sorted_max_lst[i:i + 1] for i in range(0, lst_len, lst_len - 1)]
    # return sorted_min_lst + sorted_max_lst

    # sorted_lst = sorted(lst)
    # sorted_min_lst = [sorted_lst[0]]
    # sorted_max_lst = sorted_lst[1:]
    # sorted_max_lst = sorted(sorted_max_lst, reverse=True)
    # return sorted_min_lst + sorted_max_lst

    # if not lst
