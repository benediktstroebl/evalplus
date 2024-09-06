
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
    # if lst is empty or one element, just return the same list
    if len(lst) == 0 or len(lst) == 1:
        return lst

    # initialize new_lst to be the empty list
    new_lst = []

    # initialize min_max_list to be the list of integers (in lst)
    # subtracted by the smallest element in lst
    min_max_list = []

    # find minimum value of lst
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    # remove the minimum element from lst
    lst.remove(min_value)

    # find maximum value of lst
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    # remove the maximum element from lst
    lst.remove(max_value)

    # add the minimum and maximum values to min_max_list
    min_max_list.append(min_value)
    min_max_list.append(max_value)

    # add the elements in lst to min_max_list
    min_max_list += lst

    # add the elements in min_max_list to new_lst
    for num in min_max_list:
        new_lst.append(num)

    # return new_lst
    return new_lst

