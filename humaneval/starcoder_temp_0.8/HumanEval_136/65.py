
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
    # Write your code here
    n = len(lst)
    if n == 0:
        return (None, None)
    else:
        pos = None
        neg = None
        for i in range(n):
            if lst[i] >= 0:
                pos = lst[i]
            else:
                neg = lst[i]
    return (neg, pos)
