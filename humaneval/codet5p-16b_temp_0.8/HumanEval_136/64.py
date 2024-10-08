
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

    max_num = None
    min_num = None

    for num in lst:
        if num > 0 and max_num == None:
            max_num = num
        elif num < 0 and min_num == None:
            min_num = num
        elif num < 0 and num > max_num:
            max_num = num
        elif num > 0 and num < min_num:
            min_num = num

    if min_num == None or max_num == None:
        return (None, None)
    else:
        return (max_num, min_num)
