
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

    lst1 = []
    for x in lst:
        if x > 0:
            lst1.append(x)
        if x < 0:
            lst1.append(x)

    if lst1:
        lst1.sort(reverse = True)
        return (lst1[0], lst1[-1])
    else:
        return (None, None)
