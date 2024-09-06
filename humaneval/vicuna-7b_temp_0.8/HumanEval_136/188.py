
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
    if not lst:
        return None, None

    if not lst[0] in (1, 0):
        return lst[0], lst[-1]

    largest = lst[0]
    smallest = lst[-1]
    for i in lst[1:]:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i

    return largest, smallest
