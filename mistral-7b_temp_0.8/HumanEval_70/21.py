
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
    list_1 = []
    for i in range(len(lst)):
        print(lst[i], i)
        if i == 0:
            list_1.append(lst[i])
            continue
        if i % 2 == 0:
            list_1.append(max(lst[i:]))
        else:
            list_1.append(min(lst[i:]))
    print(list_1)
    return list_1
