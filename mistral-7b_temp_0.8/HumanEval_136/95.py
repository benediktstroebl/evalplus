
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
    positive_numbers = [i for i in lst if i > 0]
    negative_numbers = [i for i in lst if i < 0]

    if not positive_numbers and not negative_numbers:
        return (None, None)
    elif not positive_numbers:
        return (None, max(negative_numbers))
    elif not negative_numbers:
        return (min(positive_numbers), None)
    else:
        return (min(negative_numbers), max(positive_numbers))
