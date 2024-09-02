
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
    if lst == [] or lst == [0]:
        return (None, None)
    else:
        negative = None
        positive = None
        for number in lst:
            if number < 0:
                negative = number
                if negative == None:
                    return (negative, None)
            elif number > 0:
                positive = number
                if positive == None:
                    return (None, positive)
        return (negative, positive)
