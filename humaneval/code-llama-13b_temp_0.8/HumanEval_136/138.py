
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
    ints_list = [i for i in lst if type(i) == int]
    if len(ints_list) == 0:
        return (None, None)

    def get_smallest_positive_int(lst):
        return min([i for i in lst if i > 0])

    def get_largest_negative_int(lst):
        return max([i for i in lst if i < 0])

    largest_negative = get_largest_negative_int(ints_list)
    smallest_positive = get_smallest_positive_int(ints_list)

    return (largest_negative, smallest_positive)
