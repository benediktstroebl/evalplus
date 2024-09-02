
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
    #
    # lst = [1, 2, 3, 4]
    #
    #
    # lst_sorted = []
    # while len(lst) > 0:
    #     # 1. 1
    #     lst_sorted.append(min(lst))
    #     lst.remove(min(lst))
    #     # 2. 4
    #     lst_sorted.append(max(lst))
    #     lst.remove(max(lst))
    #     # 3. 2
    #     lst_sorted.append(min(lst))
    #     lst.remove(min(lst))
    #     # 4. 3
    #     lst_sorted.append(max(lst))
    #     lst.remove(max(lst))
    #
    # print(lst_sorted)
    # return lst_sorted
    #
    # lst = [1, 2, 3, 4]
    #
    #
    # lst_sorted = []
    # while len(lst) > 0:
    #     lst_sorted.append(max(lst))
    #     lst.remove(max(lst))
    #     lst_sorted.append(min(lst))
    #     lst.remove(min(lst))
    #
    # print(lst_sorted)
    # return lst_sorted
    #
    # lst = [1, 2, 3, 4]
    # lst_sorted = []
    #
    # while lst:
    #     lst_sorted.append(min(lst))
    #     lst.remove(min(lst))
    #     if len(lst) > 0:
    #         lst_sorted.append(max(lst))
    #         lst.remove(max(lst))
    #
    # print(lst_sorted)
    # return lst_sorted
    #
    # lst = [1, 2, 3, 4]
    # lst_sorted = []
    #
    # while lst:
    #     lst_sorted.append(min(lst))
    #     lst.remove(min(lst))
    #
