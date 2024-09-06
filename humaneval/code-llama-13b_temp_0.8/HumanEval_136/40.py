
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
    # Solution 1
    def is_int(x):
        try:
            return int(x)
        except ValueError:
            return None

    negative_int = max([x for x in lst if is_int(x) < 0], default=None)
    positive_int = min([x for x in lst if is_int(x) > 0], default=None)
    return negative_int, positive_int
    
    # Solution 2
    # lst = list(filter(lambda x: (x.isdigit() and int(x) < 0), lst))
    # return max(lst) or None, min(lst) or None
    
    
    
