
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

    lst_negative = []
    lst_positive = []
    max_negative = None
    min_positive = None
    for num in lst:
        if num < 0:
            lst_negative.append(num)
            if max_negative == None or num > max_negative:
                max_negative = num
        elif num > 0:
            lst_positive.append(num)
            if min_positive == None or num < min_positive:
                min_positive = num
    if len(lst_negative) == 0:
        max_negative = None
    if len(lst_positive) == 0:
        min_positive = None

    return (max_negative, min_positive)

