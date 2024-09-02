
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

    # Exclude the cases in which the list is empty
    if len(lst) == 0:
        return [None, None]

    # Store the largest negative integer
    largest_negative_int = -9999999

    # Store the smallest positive integer
    smallest_positive_int = 9999999

    # Loop through the list
    for n in lst:

        # Check if the number is negative
        if n < 0:

            # If so, update the largest negative integer
            if n > largest_negative_int:
                largest_negative_int = n

        # Otherwise, check if the number is positive
        elif n > 0:

            # If so, update the smallest positive integer
            if n < smallest_positive_int:
                smallest_positive_int = n

    # Return the largest negative integer and the smallest positive integer
    return (largest_negative_int, smallest_positive_int)

