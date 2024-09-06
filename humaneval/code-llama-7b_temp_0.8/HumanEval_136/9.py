
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
    largest, smallest = None, None
    for elm in lst:
        if elm < 0 and (smallest is None or elm < smallest):
            smallest = elm
        elif elm > 0 and (largest is None or elm > largest):
            largest = elm
    return largest, smallest
