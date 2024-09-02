
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
    lst=[]
    for i in range(len(lst)):
        if lst[i] > 0:
            lst.append(lst[i])
        elif lst[i] < 0:
            lst.append(lst[i])
    a=max(lst)
    b=min(lst)
    if a > 0:
        a=None
    if b < 0:
        b=None
    return a, b

