
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
    # sort the list
    lst = sorted(lst)
    # get length
    length = len(lst)
    # create a list to return
    result = []
    # while the length is not zero
    while length > 0:
        # remove the first value
        min = lst[0]
        lst.remove(min)
        # add the first value to the result
        result.append(min)
        # get the length of the remaining list
        length = len(lst)
        # if the length is not zero
        if length > 0:
            # get the maximum value in the remaining list
            max = max(lst)
            # add that to the result
            result.append(max)
            # remove that value from the list
            lst.remove(max)
            # get the length of the remaining list
            length = len(lst)
    # return the result
    return result
