
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
    # TODO: Write solution here
    if not lst:
        return lst

    i = 0
    while i < len(lst):
        curr_val = lst[i]
        if i % 2 == 0:
            lst.remove(curr_val)
            lst.append(curr_val)
        else:
            lst.remove(curr_val)
            lst.insert(0, curr_val)
        i += 1

    return lst


