
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
    # Check if there is a negative number in the list
    if -1 in lst:
        # Check if there is a positive number in the list
        if 1 in lst:
            # Return the largest negative number and the smallest positive number
            return (-1, 1)
        # Return None for the smallest positive number
        return (None, 1)
    # Check if there are any positive numbers
    if 1 in lst:
        # Return the largest positive number
        return (lst[0],)
    # Return None for the smallest positive number
    return (None,)
