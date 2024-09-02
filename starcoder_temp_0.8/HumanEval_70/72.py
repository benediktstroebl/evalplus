
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

    # Your code here
    if len(lst) < 2:
        return lst
    sorted_list = []
    first = sorted(lst)
    for i in range(len(lst)):
        if i % 2 == 0:
            sorted_list.append(first[i])
        else:
            sorted_list.append(first[-i - 1])
    return sorted_list
