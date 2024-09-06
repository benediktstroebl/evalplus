
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

    
    lst_new = [min(lst)]
    lst_copy = [x for x in lst if x > min(lst)]
    lst_copy.sort(reverse=True)
    lst_new += lst_copy
    lst_copy = [min(lst)]
    lst_new += lst_copy
    return lst_new
