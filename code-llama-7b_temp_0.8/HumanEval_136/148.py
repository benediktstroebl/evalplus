
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
    largest_int, smallest_int = None, None

    for num in lst:
        if isinstance(num, int):
            if num < 0 and (smallest_int == None or num < smallest_int):
                smallest_int = num
            elif num > 0 and (largest_int == None or num > largest_int):
                largest_int = num

    return (largest_int, smallest_int)
