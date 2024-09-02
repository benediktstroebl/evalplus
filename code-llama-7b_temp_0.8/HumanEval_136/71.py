
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
    lst = [int(i) for i in lst]
    largest = None
    smallest = None
    for i in lst:
        if i < 0:
            if largest is None or i > largest:
                largest = i
        elif i > 0:
            if smallest is None or i < smallest:
                smallest = i

    return largest, smallest

