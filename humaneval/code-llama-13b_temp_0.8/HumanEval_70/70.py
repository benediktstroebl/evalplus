
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
    if not lst:
        return []
    max_lst = []
    min_lst = []
    new_lst = []
    for item in lst:
        if item % 2 == 0:
            max_lst.append(item)
        else:
            min_lst.append(item)
    min_lst.sort()
    max_lst.sort(reverse=True)
    for i in range(len(lst)):
        if i % 2 == 0:
            new_lst.append(min_lst[i//2])
        else:
            new_lst.append(max_lst[i//2])
    return new_lst

