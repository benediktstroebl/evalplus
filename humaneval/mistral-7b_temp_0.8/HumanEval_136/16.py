
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

    smallest = 0
    largest = 0

    if len(lst) == 0:
        return None, None
    if len(lst) == 1:
        return lst[0], lst[0]

    for n in lst:
        if n >= 0:
            if n < smallest:
                smallest = n
        if n < 0:
            if n > largest:
                largest = n
    return largest, smallest
