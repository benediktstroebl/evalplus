
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
    negative_numbers = set()
    positive_numbers = set()
    for item in lst:
        if item < 0:
            negative_numbers.add(item)
        elif item > 0:
            positive_numbers.add(item)

    negative_numbers = sorted(list(negative_numbers))
    if not negative_numbers:
        return (None, None)

    positive_numbers = sorted(list(positive_numbers))
    if not positive_numbers:
        return (None, None)

    return (max(negative_numbers), min(positive_numbers))

