
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

    # None if empty
    if not lst:
        return None, None

    # Check if negative or positive and return appropriate tuple
    if any(item < 0 for item in lst):
        return max(lst), None
    elif any(item > 0 for item in lst):
        return None, min(lst)
