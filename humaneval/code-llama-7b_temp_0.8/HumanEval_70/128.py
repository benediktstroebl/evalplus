
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
    # Our solution is to use two lists
    # A list of min values
    min_lst = []
    # A list of max values
    max_lst = []
    for val in lst:
        if len(min_lst) == 0:
            min_lst.append(val)
        elif val < min_lst[-1]:
            min_lst.append(val)
        else:
            max_lst.append(val)

    sorted_lst = []
    # Append the min values first
    sorted_lst.extend(min_lst)
    # Append the max values second
    sorted_lst.extend(max_lst)

    return sorted_lst
