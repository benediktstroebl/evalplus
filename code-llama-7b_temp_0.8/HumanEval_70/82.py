
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

    # We can use the list.sort function and specify the key function
    # lst.sort(key = lambda x: [x, -x])
    #return lst

    result = []
    while lst:
        # Find minimum value
        min_val = min(lst)
        # Add it to result
        result.append(min_val)
        # Remove it from lst
        lst.remove(min_val)
        # Get maximum value from remaining
        max_val = max(lst)
        # Add it to result
        result.append(max_val)
        # Remove it from lst
        lst.remove(max_val)

    return result
