
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
    if lst:
        largest_negative_integer = None
        smallest_positive_integer = None
        for num in lst:
            if num < 0:
                if largest_negative_integer == None or num > largest_negative_integer:
                    largest_negative_integer = num
            else:
                if smallest_positive_integer == None or num < smallest_positive_integer:
                    smallest_positive_integer = num
        return (largest_negative_integer, smallest_positive_integer)
    else:
        return (None, None)
