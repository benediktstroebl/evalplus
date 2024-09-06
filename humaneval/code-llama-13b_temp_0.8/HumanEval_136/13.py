
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
    negative_integer = []
    positive_integer = []
    for i in lst:
        if i < 0:
            negative_integer.append(i)
        elif i >= 0:
            positive_integer.append(i)
        else:
            pass
    if negative_integer == []:
        return (None, min(positive_integer))
    if positive_integer == []:
        return (max(negative_integer), None)
    return (max(negative_integer), min(positive_integer))
    
    # better answer
    # return (max(x for x in lst if x < 0), min(x for x in lst if x >= 0))
    
    # other solution
    # min_pos = max_neg = None
    # for i in lst:
    #     if i < 0 and (min_pos == None or i < min_pos):
    #         min_pos = i
    #     if i >= 0 and (max_neg == None or i > max_neg):
    #         max_neg = i
    # return (max_neg, min_pos)
    
