
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

    largest = None
    smallest = None
    if len(lst) == 0:
        return (None, None)
    for i in range(len(lst)):
        if lst[i] < 0:
            if largest == None:
                largest = lst[i]
            elif largest < lst[i]:
                largest = lst[i]
        if lst[i] > 0:
            if smallest == None:
                smallest = lst[i]
            elif smallest > lst[i]:
                smallest = lst[i]
    return (largest, smallest)
