
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
    if len(lst) < 1:
        return []
    asc = len(lst)
    desc = asc + 1
    asc_lst = [lst[0], lst[1]]
    desc_lst = [lst[0], lst[1]]
    for index in range(2, len(lst)):
        if lst[index] > asc_lst[0]:
            asc_lst = [lst[index]] + asc_lst
        elif lst[index] > asc_lst[1]:
            asc_lst.append(lst[index])
    for index in range(2, len(lst)):
        if lst[index] < desc_lst[0]:
            desc_lst = [lst[index]] + desc_lst
        elif lst[index] < desc_lst[1]:
            desc_lst.append(lst[index])
    return desc_lst[1:len(desc_lst)] + asc_lst[1:len(asc_lst)]
