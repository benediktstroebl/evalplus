
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
    smallest_positive_number = None
    largest_negative_number = None
    for item in lst:
        if isinstance(item, int):
            if (smallest_positive_number is None or item < smallest_positive_number) and item > 0:
                smallest_positive_number = item
            if (largest_negative_number is None or item > largest_negative_number) and item < 0:
                largest_negative_number = item

    return (largest_negative_number, smallest_positive_number)
