
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

    def sort_list(lst):
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return lst
        return sort_list([min(lst)] + [num for num in lst if num!= min(lst)]) + \
               sort_list([max(lst)] + [num for num in lst if num!= max(lst)])

    return sort_list(lst)
