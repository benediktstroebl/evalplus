
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
    # if there are negative and positive integers, find the largest and smallest
    if any(i < 0 for i in lst):
        largest = max(lst)
        smallest = min(lst)
        return (largest, smallest)
    # if there are no negative or positive integers, return None
    else:
        return (None, None)