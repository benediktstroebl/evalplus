
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
    # Write your code here

    #initializing min and max values for integers
    min_pos_int = 100
    min_neg_int = 0
    max_pos_int = 0
    max_neg_int = -100

    #iterate through the list
    for i in lst:
        if i < 0:
            if i < min_neg_int:
                min_neg_int = i
        else:
            if i > max_pos_int:
                max_pos_int = i

    #create tuple of min_neg_int and max_pos_int
    if max_pos_int != 0:
        return (min_neg_int, max_pos_int)
    else:
        return (min_neg_int, None)


