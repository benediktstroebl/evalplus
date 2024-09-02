
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
    # Initialize largest and smallest variables
    largest = smallest = None

    # Loop through the list
    for integer in lst:
        # Check if the integer is negative
        if integer < 0:
            # Check if the current largest is None
            if largest is None:
                # Set largest to integer
                largest = integer
            elif integer > largest:
                # Set largest to integer
                largest = integer
        # Check if the integer is positive
        elif integer > 0:
            # Check if the current smallest is None
            if smallest is None:
                # Set smallest to integer
                smallest = integer
            elif integer < smallest:
                # Set smallest to integer
                smallest = integer
    return (largest, smallest)
