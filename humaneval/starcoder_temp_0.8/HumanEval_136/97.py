
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
    if len(lst) == 0:
        return (None, None)

    largest_num = lst[0]
    smallest_num = lst[0]

    for num in lst:
        if num > largest_num and num < 0:
            largest_num = num
        elif num < smallest_num and num > 0:
            smallest_num = num

    return (largest_num, smallest_num)
