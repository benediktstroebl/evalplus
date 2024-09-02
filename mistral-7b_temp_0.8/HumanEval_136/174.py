
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
    smallest_num = lst[0]
    largest_num = lst[0]
    if lst[0] > 0:
        smallest_num = lst[0]
    else:
        largest_num = lst[0]
    for n in lst[1:]:
        if n > largest_num and n < 0:
            largest_num = n
        elif n < smallest_num and n > 0:
            smallest_num = n
    if largest_num == None or smallest_num == None:
        return None, None
    return largest_num, smallest_num
