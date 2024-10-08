
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

    # Write your code here
    largest_neg = None
    smallest_pos = None

    for x in lst:
        if x < 0:
            if largest_neg == None or x > largest_neg:
                largest_neg = x

        if x > 0:
            if smallest_pos == None or x < smallest_pos:
                smallest_pos = x

    if largest_neg == None:
        return None, None

    return largest_neg, smallest_pos
