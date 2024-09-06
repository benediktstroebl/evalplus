
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

    # raise NotImplementedError()
    # must use list comprehension
    # https://stackoverflow.com/questions/136097/what-is-the-difference-between-list-and-dict-in-python
    # check if lst is empty
    if len(lst) == 0:
        return lst
    lst_dict = {}
    for index, value in enumerate(lst):
        if value not in lst_dict:
            lst_dict[value] = [index]
        else:
            lst_dict[value].append(index)
    min_lst = [min(lst_dict)]
    max_lst = [max(lst_dict)]
    while len(lst_dict[min(lst_dict)]) != 0:
        min_lst.append(max(lst_dict[min(lst_dict)]))
        del lst_dict[min(lst_dict)][lst_dict[min(lst_dict)].index(max(lst_dict))]
        lst_dict[min(lst_dict)].append(min(lst_dict))
    while len(lst_dict[max(lst_dict)]) != 0:
        max_lst.append(min(lst_dict[max(lst_dict)]))
        del lst_dict[max(lst_dict)][lst_dict[max(lst_dict)].index(min(lst_dict))]
        lst_dict[max(lst_dict)].append(max(lst_dict))
    return [lst[i] for i in min_lst+max_lst[1:]]
    # # return list comprehension
    # if len(lst) < 2:
    #     return lst
    # # else:
    # #     min_lst = [min(lst)]
    # #     max_lst = [max(lst)]
    # #     while len(lst) != 0:
    # #         min_lst.append(max(lst))
    # #         del lst[lst.index(max(lst))]
    # #         lst.append(min(lst))
    # #     while len(lst) != 0:
    # #         max_
