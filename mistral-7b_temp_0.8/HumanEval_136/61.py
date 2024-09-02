
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
    smallest_number = None
    largest_number = None
    for number in lst:
        if number < 0:
            if largest_number is None or number > largest_number:
                largest_number = number
        elif number > 0:
            if smallest_number is None or number < smallest_number:
                smallest_number = number
    return largest_number, smallest_number
