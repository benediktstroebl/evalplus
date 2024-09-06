
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
    # Create a function that returns the largest integer and smallest integer
    # If there are none return none
    def largest_smallest(lst):
        max_int = max([-x for x in lst if x < 0])
        min_int = min([x for x in lst if x > 0 ])
        if max_int < 0:
            return (None, max_int)
        elif min_int > 0:
            return (min_int, None)
        else:
            return (None, None)

    # Call the function
    return largest_smallest(lst)
