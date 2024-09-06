
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
    def compare_to_last(val, lst):
        if val < lst[-1]:
            return 1
        elif val > lst[-1]:
            return -1
        else:
            return 0

    lst_length = len(lst)
    while lst_length > 1:
        for i in xrange(0, lst_length - 1, 2):
            if compare_to_last(lst[i], lst[i + 1:]) == 1:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        lst_length -= 1
    return lst

