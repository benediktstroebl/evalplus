
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
    negative_ints_list = [int(x) for x in lst if int(x) < 0]
    positive_ints_list = [int(x) for x in lst if int(x) > 0]
    if not negative_ints_list:
        negative_ints_list = None
    if not positive_ints_list:
        positive_ints_list = None

    return (negative_ints_list, positive_ints_list)

