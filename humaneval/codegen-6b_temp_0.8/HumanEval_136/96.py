
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
    if all(isinstance(i, int) for i in lst):
        lst.sort()
        n1, n2 = None, None
        for i, l in enumerate(lst):
            if l < 0:
                n1 = l
                if n1 == lst[i-1]:
                    continue
                n2 = lst[i+1]
            if n1 is None and n2 is None:
                return None, None
            if n1 is None and n2 is not None:
                return n1, n2
            if n2 is None and n1 is not None:
                return n1, n2
        return n1, n2
    else:
        return None, None
