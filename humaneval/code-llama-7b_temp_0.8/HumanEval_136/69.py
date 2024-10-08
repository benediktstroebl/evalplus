
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
    if not lst:
        return None, None
    else:
        largest_num = None
        smallest_num = None
        for i in lst:
            if i < 0:
                if not largest_num:
                    largest_num = i
                if i > largest_num:
                    largest_num = i
            if i > 0:
                if not smallest_num:
                    smallest_num = i
                if i < smallest_num:
                    smallest_num = i
        return largest_num, smallest_num

