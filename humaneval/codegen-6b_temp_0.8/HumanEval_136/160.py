
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
    #a = sorted(lst, reverse=True)
    #b = sorted(lst)
    #return (max(a),min(b)) if len(a)>0 and len(b)>0 else (None,None)

    # one liner
    return (max(sorted(filter(lambda x: x<0, lst),reverse=True)[0] if len(filter(lambda x: x<0, lst))>0 else None,\
                min(sorted(filter(lambda x: x>0, lst),reverse=True)[0] if len(filter(lambda x: x>0, lst))>0 else None)))
           