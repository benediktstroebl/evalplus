
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
    negative_ints = [i for i in lst if i < 0]
    positive_ints = [i for i in lst if i > 0]
    if len(negative_ints) == 0 and len(positive_ints) == 0:
        return None, None
    if len(negative_ints) == 0:
        return None, max(positive_ints)
    if len(positive_ints) == 0:
        return min(negative_ints), None
    return min(negative_ints), max(positive_ints)

