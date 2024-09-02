
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
    if lst == []:
        return lst

    new_list = []
    if lst[0] < lst[-1]:
        return lst

    for i in range(len(lst)//2):
        new_list.append(lst[-1])
        new_list.append(lst[i])

    return new_list
