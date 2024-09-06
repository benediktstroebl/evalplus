
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

    # this will be our sorted list
    sorted_list = []

    # here we are doing our sorting
    while len(lst) > 0:
        # find the min value
        min_val = min(lst)
        # remove it from the original list
        lst.remove(min_val)

        # add the min val to our sorted list
        sorted_list.append(min_val)

    # return our sorted list
    return sorted_list
