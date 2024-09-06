
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
    # return (None, None) if lst is empty or if there are no ints
    # or there are no negative or positive ints
    if not lst or len([x for x in lst if type(x) == int]) == 0:
        return None, None

    # find the biggest negative int in the list
    negative_int = max([x for x in lst if x < 0])

    # find the smallest positive int in the list
    positive_int = min([x for x in lst if x > 0])

    # return as a tuple
    return negative_int, positive_int
