
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

    
    negative_list = []
    positive_list = []

    for i in lst:
        if i < 0:
            negative_list.append(i)
        elif i > 0:
            positive_list.append(i)

    if len(negative_list) == 0:
        a = None
    else:
        a = max(negative_list)

    if len(positive_list) == 0:
        b = None
    else:
        b = min(positive_list)

    return (a, b)
