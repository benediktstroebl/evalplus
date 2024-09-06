
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
    new_list = []
    while len(lst) != 0:
        temp_min = lst[0]
        for i in lst:
            if i < temp_min:
                temp_min = i
        new_list.append(temp_min)
        lst.remove(temp_min)

    for i in range(len(lst)):
        temp_max = lst[0]
        for j in lst:
            if j > temp_max:
                temp_max = j
        new_list.append(temp_max)
        lst.remove(temp_max)

    return new_list

