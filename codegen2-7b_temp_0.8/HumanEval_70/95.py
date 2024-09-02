
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
    smallest = lst[0]
    biggest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
        if lst[i] > biggest:
            biggest = lst[i]
    return [smallest, *strange_sort_list(lst[1:-1]), biggest
