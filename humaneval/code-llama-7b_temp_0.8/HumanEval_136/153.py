
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
    print(f"\n\n Problem -- largest_smallest_integers({lst})")
    # your code goes here
    largest_neg = None
    smallest_pos = None
    for i in lst:
        if type(i) is int and i < 0:
            if largest_neg == None:
                largest_neg = i
            elif i > largest_neg:
                largest_neg = i
        if type(i) is int and i > 0:
            if smallest_pos == None:
                smallest_pos = i
            elif i < smallest_pos:
                smallest_pos = i
    if largest_neg == None and smallest_pos == None:
        return (None, None)
    elif largest_neg == None:
        return (None, smallest_pos)
    elif smallest_pos == None:
        return (largest_neg, None)
    else:
        return (largest_neg, smallest_pos)



