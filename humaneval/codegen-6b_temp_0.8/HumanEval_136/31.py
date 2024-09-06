
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
    
    negative = [number for number in lst if number < 0]
    positive = [number for number in lst if number > 0]
    if negative and positive:
        return (negative[0], positive[0])
    elif negative:
        return (negative[0], None)
    elif positive:
        return (None, positive[0])
    else:
        return (None, None)
