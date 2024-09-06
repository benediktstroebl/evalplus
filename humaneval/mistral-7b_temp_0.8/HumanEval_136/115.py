
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
    # Initialize a tuple that will hold the largest negative integer and smallest positive integer
    # If there are no negative or positive integers, set the values to None
    (a, b) = (None, None)

    # Loop through the list of integers
    for x in lst:
        # If x is a negative integer, check if it is larger than the current largest negative integer
        if x < 0:
            if a is None or x > a:
                a = x
        # If x is a positive integer, check if it is smaller than the current smallest positive integer
        elif x > 0:
            if b is None or x < b:
                b = x

    # Return the tuple (a, b)
    return a, b
