
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
    neg_count = 0
    pos_count = 0
    largest = lst[0]
    smallest = lst[-1]
    for num in lst:
        if num < 0:
            neg_count += 1
        elif num > 0:
            pos_count += 1
        elif num == 0:
            largest = -1
            smallest = 0
        elif neg_count > pos_count:
            largest = -1
        elif pos_count > neg_count:
            smallest = 0
    return largest, smallest
