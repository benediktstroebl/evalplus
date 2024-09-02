
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
    large = None
    small = None

    for item in lst:
        if type(item) is not int:
            raise TypeError('The item is not an integer')
        if item < 0:
            large = max(large, item)
        elif item > 0:
            small = min(small, item)

    return (large, small)
