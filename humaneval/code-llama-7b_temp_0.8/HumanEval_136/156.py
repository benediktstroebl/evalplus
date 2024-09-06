
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
    largest_negative = None
    smallest_positive = None
    for integer in lst:
        if integer < 0 and integer > largest_negative:
            largest_negative = integer
        elif integer > 0 and integer < smallest_positive:
            smallest_positive = integer
    return (largest_negative, smallest_positive)
