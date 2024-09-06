
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
    if len(lst) == 0:
        return []

    # use array to store current value
    # for each value, compare with current value, move it to the head
    # if a number is smaller than or equal to the current value,
    # update the value to current value
    # also compare the last value with the current value
    ## O(n) time, O(n) space
    value = [lst.pop(0)]
    for val in lst:
        if val <= value[0]:
            value[0] = val
        elif val > value[-1]:
            value.append(val)

    return value

