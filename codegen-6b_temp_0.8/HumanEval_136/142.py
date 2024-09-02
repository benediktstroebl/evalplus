
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
    num_negative = [i for i in lst if i < 0]
    num_positive = [i for i in lst if i > 0]
    if num_negative:
        a = max(num_negative)
    else:
        a = None
    if num_positive:
        b = min(num_positive)
    else:
        b = None
    return (a,b)
