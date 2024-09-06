
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

    if len(lst) == 0:
        return None, None
    negative_values = []
    positive_values = []
    for i in lst:
        if i < 0:
            negative_values.append(i)
        elif i > 0:
            positive_values.append(i)

    if negative_values == []:
        return None, min(positive_values)
    elif positive_values == []:
        return max(negative_values), None
    else:
        return max(negative_values), min(positive_values)

