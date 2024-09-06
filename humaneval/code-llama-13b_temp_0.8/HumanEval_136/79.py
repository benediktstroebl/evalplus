
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
    int_list = list(filter(lambda x: type(x) == int, lst))
    if len(int_list) == 0:
        return (None, None)
    elif len(int_list) == 1:
        return (None, None)
    
    largest_neg = int_list[0]
    smallest_pos = int_list[0]
    for i in int_list[1:]:
        if i > largest_neg and i < 0:
            largest_neg = i
        if i < smallest_pos and i > 0:
            smallest_pos = i
    return (largest_neg, smallest_pos)

    
