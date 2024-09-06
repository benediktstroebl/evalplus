
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
    lowest = None
    highest = None
    for i in lst:
        if type(i) == int:
            if highest == None:
                if i >= 0:
                    highest = i
            else:
                if i > highest and i >= 0:
                    highest = i
            if lowest == None:
                if i <= 0:
                    lowest = i
            else:
                if i < lowest and i <= 0:
                    lowest = i
    return (lowest, highest)
