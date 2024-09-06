
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
    neg = [i for i in lst if i < 0]
    pos = [i for i in lst if i > 0]
    if len(neg) == 0 and len(pos) == 0:
        return None, None
    elif len(neg) == 0:
        return pos[0], None
    elif len(pos) == 0:
        return None, neg[0]
    else:
        return neg[0], pos[0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(largest_smallest_integers(lst))
