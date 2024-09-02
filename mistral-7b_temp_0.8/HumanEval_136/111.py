
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

    # your code here

    # Create a tuple to store the largest negative integer and the smallest positive integer
    largest_negative_integer = None
    smallest_positive_integer = None

    # Loop through the list of integers
    for integer in lst:
        # If the integer is negative and the largest_negative_integer is None or the integer is greater than the largest_negative_integer, update the largest_negative_integer
        if integer < 0 and (largest_negative_integer is None or integer > largest_negative_integer):
            largest_negative_integer = integer
        # If the integer is positive and the smallest_positive_integer is None or the integer is less than the smallest_positive_integer, update the smallest_positive_integer
        elif integer > 0 and (smallest_positive_integer is None or integer < smallest_positive_integer):
            smallest_positive_integer = integer

    # Return a tuple with the largest negative integer and the smallest positive integer
    return largest_negative_integer, smallest_positive_integer
