
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
    # Find the largest negative integer
    negative = [i for i in lst if i < 0]
    if negative != []:
        max_negative = max(negative)
    else:
        max_negative = None

    # Find the smallest positive integer
    positive = [i for i in lst if i > 0]
    if positive != []:
        min_positive = min(positive)
    else:
        min_positive = None

    return max_negative, min_positive

