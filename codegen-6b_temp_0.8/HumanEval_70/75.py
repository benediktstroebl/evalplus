
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
    if len(lst) == 0:
        return []

    min_val = lst[0]
    max_val = lst[-1]

    min_index = 0
    max_index = len(lst) - 1

    for i in range(len(lst)):
        print(lst[i])
        if lst[i] < min_val:
            min_val = lst[i]
            min_index = i
        if lst[i] > max_val:
            max_val = lst[i]
            max_index = i

    new_lst = [min_val]

    for i in range(min_index + 1, max_index):
        new_lst.append(lst[i])

    new_lst.append(max_val)

    return new_lst
