
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    def find_max(lst):
        ''' Find the max value in a list '''
        max_value = None
        for l in lst:
            if l > max_value:
                max_value = l
        return max_value

    def find_min(lst):
        ''' Find the min value in a list '''
        min_value = None
        for l in lst:
            if l < min_value or min_value is None:
                min_value = l
        return min_value
    # Test case #1
    lst_test = [1, 2, 3, 4, 6, 7]
    assert (find_max(lst_test), find_min(lst_test)) == (6, 1)
    # Test case #2
    lst_test = [-1, -2, -3, -4, -6, -7]
    assert (find_max(lst_test), find_min(lst_test)) == (None, -1)

