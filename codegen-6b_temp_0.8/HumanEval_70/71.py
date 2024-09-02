
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
        return []
    else:
        new_list = [lst[0]]
        minimum = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < minimum:
                minimum = lst[i]
            new_list.append(minimum)
        new_list.append(lst[-1])
        for i in range(1, len(lst)):
            if lst[-i] > minimum:
                new_list.append(lst[-i])
            else:
                new_list.append(minimum)
        return new_list
