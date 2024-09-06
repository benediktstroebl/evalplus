
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
    # My Implementation
    # largest_neg_int = None
    # smallest_pos_int = None
    # for i in lst:
    #     if i < 0 and largest_neg_int < i:
    #         largest_neg_int = i
    #     elif i > 0 and smallest_pos_int > i:
    #         smallest_pos_int = i
    # return (largest_neg_int, smallest_pos_int)

    # List Comprehension Implementation
    largest_neg_int = None
    smallest_pos_int = None
    for i in [num for num in lst if num < 0]:
        largest_neg_int = i if i > largest_neg_int else largest_neg_int
    for i in [num for num in lst if num > 0]:
        smallest_pos_int = i if i < smallest_pos_int else smallest_pos_int
    return (largest_neg_int, smallest_pos_int)

