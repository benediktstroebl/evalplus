
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
    if len(lst) > 0:
        negative_list = [x for x in lst if x < 0]
        positive_list = [x for x in lst if x >= 0]

        if len(negative_list) > 0:
            return min(negative_list), None
        else:
            return None, max(positive_list)
    else:
        return None
