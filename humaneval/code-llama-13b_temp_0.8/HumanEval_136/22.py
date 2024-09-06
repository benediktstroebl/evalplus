
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
    largest_negative, smallest_positive = (None, None)
    for el in lst:
        if type(el) == int:
            if el < 0:
                if largest_negative == None or el > largest_negative:
                    largest_negative = el
            elif el > 0:
                if smallest_positive == None or el < smallest_positive:
                    smallest_positive = el
    return largest_negative, smallest_positive
