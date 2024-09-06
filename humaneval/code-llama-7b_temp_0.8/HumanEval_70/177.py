
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

    # if the list is empty
    if len(lst) == 0:
        return []

    # return the list in reverse order
    lst = lst[::-1]

    # while the list has more than 1 item
    while len(lst) > 1:
        # add the smallest number to the list
        lst.append(lst[0])
        # remove the smallest number from the list
        lst = lst[1:]
        # reverse the list
        lst = lst[::-1]

    # return the list
    return lst

