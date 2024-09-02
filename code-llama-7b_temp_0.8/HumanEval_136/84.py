
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
    #your code here
    all_pos = []
    all_neg = []
    for i in lst:
        if i < 0:
            all_neg.append(i)
        if i > 0:
            all_pos.append(i)
    if len(all_neg) == 0 and len(all_pos) == 0:
        return (None, None)
    if len(all_neg) == 0:
        return (None, min(all_pos))
    if len(all_pos) == 0:
        return (max(all_neg), None)
    else:
        return (max(all_neg), min(all_pos))
