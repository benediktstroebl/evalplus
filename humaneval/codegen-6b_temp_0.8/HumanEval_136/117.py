
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
        return [None, None]
    negative_num = None
    negative_num_index = None
    positive_num = None
    positive_num_index = None
    for index, num in enumerate(lst):
        if num < 0:
            if negative_num_index == None:
                negative_num = num
                negative_num_index = index
            elif num < negative_num:
                negative_num = num
                negative_num_index = index
        elif num > 0:
            if positive_num_index == None:
                positive_num = num
                positive_num_index = index
            elif num > positive_num:
                positive_num = num
                positive_num_index = index
    return (negative_num, positive_num)
