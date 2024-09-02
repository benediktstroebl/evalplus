
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
        return lst

    n = len(lst)
    idx = 0
    new_list = [lst[0]]

    while idx < n:
        if idx % 2 == 0:
            new_list.append(max(lst[idx + 1 :]))
        else:
            new_list.append(min(lst[idx + 1 :]))

        idx += 1

    return new_list

