
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

    # YOUR CODE HERE
    smallest = None
    largest = None
    for x in lst:
        if x < 0 and largest == None:
            largest = x
        if x > 0 and smallest == None:
            smallest = x
        if x < 0 and x > largest:
            largest = x
        if x > 0 and x < smallest:
            smallest = x
    return largest, smallest
