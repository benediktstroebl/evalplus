
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

    if len(lst) == 0:
        return (None, None)

    biggest_negative = None
    smallest_positive = None

    for i in lst:
        if i < 0 and (biggest_negative == None or i > biggest_negative):
            biggest_negative = i
        if i > 0 and (smallest_positive == None or i < smallest_positive):
            smallest_positive = i

    return (biggest_negative, smallest_positive)

