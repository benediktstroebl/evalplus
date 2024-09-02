
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
    lst.sort()
    new_lst = []
    min = lst[0]
    max = lst[len(lst)-1]
    new_lst.append(min)
    new_lst.append(max)
    for i in range(len(lst)-2):
        if i % 2 == 0:
            new_lst.append(min)
            new_lst.append(max)
        else:
            new_lst.append(max)
            new_lst.append(min)
    return new_lst
