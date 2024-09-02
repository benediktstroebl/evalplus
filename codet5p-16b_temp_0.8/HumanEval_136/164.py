
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

    negative_numbers = []
    positive_numbers = []
    for x in lst:
        if x < 0:
            negative_numbers.append(x)
        else:
            positive_numbers.append(x)
    if len(negative_numbers) > 0:
        a = max(negative_numbers)
    else:
        a = None
    if len(positive_numbers) > 0:
        b = min(positive_numbers)
    else:
        b = None
    return (a, b)
