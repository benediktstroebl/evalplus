
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

    temp_lst = []
    for i in range(len(lst)):
        min_max = max(lst[i], lst[-1-i])
        temp_lst.append(min_max)
        lst.remove(min_max)

    return temp_lst

