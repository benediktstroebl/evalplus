
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
    # I assume this is a challenge where it's not ok to import modules.
    # But if you're allowed to, you should do it!
    # return sorted(lst, reverse=True)

    # Split the list into a list of minima, maxima, and middle-grounds.
    # Sort the list of maxima, and add them to a new list.
    # Sort the middle-grounds, and add them to a new list.
    # Return the list of minimums, plus the maxima and middle-grounds.

    def get_min_max(lst):
        '''
        Return the minimum and maximum of a list.
        Assume the list is not empty.
        '''
        # Pick the first value as the minimum.
        min_val = lst[0]
        max_val = lst[0]
        # Look through the list. If we find a value that's lower than
        # the current minimum, then change the minimum.
        # Do the same for the maximum.
        for x in lst[1:]:
            if x < min_val:
                min_val = x
            if x > max_val:
                max_val = x
        return min_val, max_val

    def sort_list(lst):
        '''
        Given a list of integers, return a list of integers sorted in
        strange order.
        '''
        # If the list is empty, return an empty list.
        if not lst:
            return []
        # If the list has only one value, return that value.
        if len(lst) == 1:
            return lst
        # Split the list into a list of minimums, a list of maximums,
        # and a list of middle-grounds.
        min_max_mid = split_into_min_max_mid(lst)
        # Sort the middle-grounds.
        # Return the list of minimums, plus the maximums and middle-grounds.
        return min_max_mid[0] + sort_list(min_max_mid[2]) + min_max_mid[1]

    def split_into_min_max_mid(lst):
        '''
        Given
