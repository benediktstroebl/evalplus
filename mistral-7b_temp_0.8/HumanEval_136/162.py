
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
    lst_new = list(filter(lambda x: x<0, lst))
    lst_new2 = list(filter(lambda x: x>0, lst))

    if lst_new and lst_new2:
        lst_new.sort()
        lst_new2.sort()
        return lst_new[-1], lst_new2[0]

    return None, None
