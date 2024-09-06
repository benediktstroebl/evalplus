
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
    # collect container for unsorted elements
    unsorted_elements = lst[:]
    # sort and collect result
    sort_lst = []
    while lst:
        # get minimum value
        min_value = min(unsorted_elements)
        # get max of rest ints
        max_value = max(unsorted_elements)
        # remove those which are between min and max
        lst = [e for e in lst if e not in range(min_value, max_value)]
        # make min_value max_value
        sort_lst.append(max_value)
        unsorted_elements.remove(max_value)
    return sort_lst

