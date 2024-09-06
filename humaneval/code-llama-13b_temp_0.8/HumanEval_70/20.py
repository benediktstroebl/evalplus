
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
    # check if there is any element in the list
    if len(lst) <= 1:
        return lst
    # check if all elements are the same
    if lst.count(lst[0]) == len(lst):
        return lst
    # check if list has even number of elements
    if len(lst) % 2 != 0:
        lst.append(lst[-1])
    # create new empty list
    lst2 = []
    # loop while the list is not empty
    while lst:
        # get minimum element
        lst2.append(min(lst))
        # remove the minimum element from the list
        lst.remove(lst2[-1])
        # get maximum element
        lst2.append(max(lst))
        # remove the maximum element from the list
        lst.remove(lst2[-1])
    # return new list
    return lst2

