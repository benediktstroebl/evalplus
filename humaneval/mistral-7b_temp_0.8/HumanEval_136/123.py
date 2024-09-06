
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

    positive_smallest = None
    negative_largest = None

    for i in lst:
        if i > 0 and positive_smallest == None:
            positive_smallest = i
        elif i > 0 and i < positive_smallest:
            positive_smallest = i

        if i < 0 and negative_largest == None:
            negative_largest = i
        elif i < 0 and i > negative_largest:
            negative_largest = i

    return negative_largest, positive_smallest

