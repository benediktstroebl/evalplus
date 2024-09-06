
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
    largest_num = smallest_num = None
    for num in lst:
        if isinstance(num, int):
            if num < 0 and (largest_num == None or num > largest_num):
                largest_num = num
            elif num > 0 and (smallest_num == None or num < smallest_num):
                smallest_num = num
    return (largest_num, smallest_num)
