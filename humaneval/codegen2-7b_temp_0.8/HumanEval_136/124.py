
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
    largest = -1*sys.maxsize
    smallest = sys.maxsize
    for number in lst:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    if smallest == -1*sys.maxsize:
        smallest = None
    if largest == sys.maxsize:
        largest = None
    return (largest, smallest)
