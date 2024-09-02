
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
    def _largest_smallest_integers(lst):
        # setting up empty list for 0 and 1
        nines, ones = [], []

        # converting to integer
        lst = [int(i) for i in lst]

        # adding negative number to list
        for i in lst:
            if i < 0:
                nines.append(i)
        # adding positive number to list
        for i in lst:
            if i > 0:
                ones.append(i)
        # returning none if no negatives or positives
        if len(nines) == 0 and len(ones) == 0:
            return None, None
        # returning ones at index 0
        elif len(ones) > 0:
            return ones, None
        # returning ones at index 1
        else:
            return nines, ones[0]
    # passing in list
    a, b = _largest_smallest_integers(lst)
    return a, b
