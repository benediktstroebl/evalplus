
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

    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]

    if negative_integers:
        largest_negative_integer = min(negative_integers)
        smallest_positive_integer = min(positive_integers)
    else:
        largest_negative_integer = None
        smallest_positive_integer = min(positive_integers) if positive_integers else None

    return (largest_negative_integer, smallest_positive_integer)
