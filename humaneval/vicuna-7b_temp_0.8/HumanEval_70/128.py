
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
    # If the list is empty return an empty list
    if not lst:
        return []
    else:
        # First check the last two values
        last_two = [lst[-1], lst[-2]]
        # If the last two values are same, then sort again
        if last_two[0] == last_two[1]:
            last_two = [lst[-2], lst[-1]]
        # If the last two values are not same, then return the list
        else:
            return lst
