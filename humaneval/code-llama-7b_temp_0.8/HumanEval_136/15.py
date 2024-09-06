
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

    largest = None
    smallest = None

    # Create a tuple of all the integers in the list
    integers = tuple(int(i) for i in lst if type(i) == int)
    # Search the integers tuple for positive and negative integers
    for i in integers:
        if i > 0:
            if largest is None:
                largest = i
            elif i > largest:
                largest = i

        if i < 0:
            if smallest is None:
                smallest = i
            elif i < smallest:
                smallest = i

    return (largest, smallest)

