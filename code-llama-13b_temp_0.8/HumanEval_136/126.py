
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
    largest = 0
    smallest = 0
    negative = False
    positive = False
    for item in lst:
        if item < 0:
            negative = True
            if largest == 0:
                largest = item
            elif largest < item:
                largest = item
        if item > 0:
            positive = True
            if smallest == 0:
                smallest = item
            elif smallest > item:
                smallest = item
    if negative:
        largest = largest
    if positive:
        smallest = smallest
    if negative == False and positive == False:
        largest = None
        smallest = None
    if negative == False and positive == True:
        largest = None
    if negative == True and positive == False:
        smallest = None
    return largest, smallest

