
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
    # sort list in descending order
    sorted_lst = sorted(lst, reverse=True)
    # init output list
    output = []
    for i in range(0, len(sorted_lst), 2):
        output.append(sorted_lst[i])
        output.append(sorted_lst[i+1])
    return output
