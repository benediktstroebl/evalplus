
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
    new_lst = []
    while lst:
        min = min(lst)
        lst.remove(min)
        new_lst.append(min)
        max = max(lst)
        lst.remove(max)
        new_lst.append(max)
    return new_lst
