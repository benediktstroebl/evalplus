
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
    def _find_min_max(lst):
        '''Finds the minimum and maximum values of list'''
        minimum = lst[0]
        maximum = lst[0]
        for number in lst[1:]:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return minimum, maximum
    lst_list = []
    for number in lst:
        lst_list.append(number)
    return _find_min_max(lst_list
