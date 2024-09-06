
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

    smallest = lst[0]
    largest = lst[0]
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
        if lst[i] > largest:
            largest = lst[i]
    if smallest < 0 and largest > 0:
        return (largest, smallest)
    elif largest < 0:
        return (None, smallest)
    elif smallest > 0:
        return (largest, None)
    else:
        return (None, None)

