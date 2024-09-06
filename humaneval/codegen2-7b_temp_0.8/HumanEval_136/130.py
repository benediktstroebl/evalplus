
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
    largest_positive = max(lst)
    smallest_negative = min(lst)
    if largest_positive < 0 and smallest_negative > 0:
        return (largest_positive, smallest_negative)
    if largest_positive > 0:
        return (largest_positive, None)
    if smallest_negative < 0:
        return (None, smallest_negative)
    return (None, None)

