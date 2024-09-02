
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
    l = [i for i in lst if type(i) is int]
    if l == []:
        return (None, None)
    elif l == lst:
        return (None, None)
    elif l == None:
        return (None, None)
    else:
        l.sort(reverse = True)
        return (l[0], l[-1])

