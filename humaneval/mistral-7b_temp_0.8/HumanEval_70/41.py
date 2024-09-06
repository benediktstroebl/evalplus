
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
    # create an empty list
    new_lst = []
    # loop through the given list
    for i in range(len(lst)):
        # find the minimum value in the remaining list
        minimum = min(lst[i:])
        # remove the minimum value from the remaining list
        lst.remove(minimum)
        # add the minimum value to the new list
        new_lst.append(minimum)
    # return the new list
    return new_lst
