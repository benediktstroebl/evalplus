
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
    neg = None
    pos = None
    for num in lst:
        if isinstance(num, int):
            if num < 0:
                if neg is None:
                    neg = num
                elif num > neg:
                    neg = num
            else:
                if pos is None:
                    pos = num
                elif num < pos:
                    pos = num
    return neg, pos
    
    # shorter solution
    # return (max([i for i in lst if i < 0]), min([i for i in lst if i >= 0]))
