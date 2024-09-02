
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
    neg_nums = []
    pos_nums = []
    for num in lst:
        if num < 0:
            neg_nums.append(num)
        elif num > 0:
            pos_nums.append(num)
    if len(neg_nums) > 0:
        negative = max(neg_nums)
    else:
        negative = None
    if len(pos_nums) > 0:
        positive = min(pos_nums)
    else:
        positive = None
    return negative, positive
    
