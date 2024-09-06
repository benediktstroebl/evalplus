
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
    # Make a list containing tuples (num, index)
    lst_tuples = [(val, idx) for idx, val in enumerate(lst)]
    # Sort the tuples by "n" (the first item in the tuple)
    lst_tuples.sort(key=itemgetter(0), reverse=True)
    # Get the sorted lst and its indices
    lst, indices = [], []
    for tup in lst_tuples:
        lst.append(tup[0])
        indices.append(tup[1])
    return [lst[idx] for idx in indices]
