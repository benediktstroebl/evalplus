
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
    numbers = sorted(lst)
    if all(x < 0 for x in numbers):
        return (-numbers[0], None)
    elif all(x > 0 for x in numbers):
        return (None, numbers[0])
    else:
        return None, None
