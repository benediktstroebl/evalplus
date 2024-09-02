
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
    for item in lst:
        if isinstance(item, int):
            if item < 0:
                if largest is None or item > largest:
                    largest = item
            elif item > 0:
                if smallest is None or item < smallest:
                    smallest = item
    return largest, smallest
