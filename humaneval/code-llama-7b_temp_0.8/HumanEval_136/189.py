
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
    #my code
    min_pos = 0
    max_neg = 0
    for i in lst:
        if i > 0 and i > max_neg:
            max_neg = i
        elif i < 0 and i < min_pos:
            min_pos = i
    if min_pos == 0 or max_neg == 0:
        return (None, None)
    return (min_pos, max_neg)

    #best answer
    max_neg = -10000
    min_pos = 10000
    for num in lst:
        if num < min_pos and num > 0:
            min_pos = num
        elif num > max_neg and num < 0:
            max_neg = num

    return max_neg, min_pos

