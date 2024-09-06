
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
    if not lst:
        return None, None
    negative_integers = [int(x) for x in lst if int(x) < 0]
    positive_integers = [int(x) for x in lst if int(x) > 0]
    return max(negative_integers) if negative_integers else None, min(positive_integers) if positive_integers else None
