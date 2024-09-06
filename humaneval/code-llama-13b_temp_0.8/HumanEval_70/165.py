
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

    # check the input is a list
    if not isinstance(lst, list):
        raise TypeError('The input must be a list')

    # check if the list is empty
    if len(lst) == 0:
        return lst

    # create a new list
    result = []
    temp = lst.copy()

    # while the temp list is not empty
    while temp != []:
        # find the minimum element in the temp list
        min_el = min(temp)
        # find the maximum element in the temp list
        max_el = max(temp)
        # append the minimum element to the result list
        result.append(min_el)
        # remove the minimum element from the temp list
        temp.remove(min_el)
        # append the maximum element to the result list
        result.append(max_el)
        # remove the maximum element from the temp list
        temp.remove(max_el)

    return result

