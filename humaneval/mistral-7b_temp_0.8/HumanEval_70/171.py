
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
    # return list(sorted(lst, reverse=True))

    # def select_min(lst):
    #     if lst:
    #         return min(lst)

    # def select_max(lst):
    #     if lst:
    #         return max(lst)

    # new_lst = []
    # while lst:
    #     new_lst.append(select_min(lst))
    #     lst.remove(select_min(lst))
    #     lst.remove(select_max(lst))

    # return new_lst

    new_lst = []
    while lst:
        new_lst.append(lst.pop(lst.index(min(lst))))
        new_lst.append(lst.pop(lst.index(max(lst))))
    return new_lst

    # return new_lst
