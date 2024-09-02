
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
    result = (None, None)

    # your code goes here
    if lst:
        pos_list = [i for i in lst if i > 0]
        neg_list = [i for i in lst if i < 0]

        if pos_list:
            result = (min(pos_list), min(neg_list)) if neg_list else (None, min(pos_list))
        elif neg_list:
            result = (None, min(neg_list))

    return result
