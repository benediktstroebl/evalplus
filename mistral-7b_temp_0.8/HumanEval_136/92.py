
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

    # write your code here
    lst = [1, 3, -5, -6, 7, 9]
    for i in lst:
        if i > 0:
            smallest_positive_number = i
        elif i < 0:
            largest_negative_number = i
        else:
            pass
    if smallest_positive_number == None:
        return None
    if largest_negative_number == None:
        return None
    return (largest_negative_number, smallest_positive_number)


