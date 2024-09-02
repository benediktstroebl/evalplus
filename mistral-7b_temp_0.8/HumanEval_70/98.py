
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
    # Sort the list of numbers into ascending order
    list = sorted(lst)
    # Starting with the minimum element, iterate over the list
    for i in range(len(list)):
        # find the maximum of the remaining elements
        max_element = max(list[i:])
        # add the maximum element to the result list
        result.append(max_element)
        # remove the maximum element from the list
        list.remove(max_element)
    return result




