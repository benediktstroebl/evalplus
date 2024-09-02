
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
    # your code here

    if len(lst) == 0:
        return lst
    lst.sort()
    new_list = []
    for i in lst:
        if i in new_list:
            new_list.remove(i)
        else:
            new_list.append(i)
    return new_list



