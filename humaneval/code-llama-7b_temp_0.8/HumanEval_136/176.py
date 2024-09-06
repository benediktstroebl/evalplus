
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

    def largest_integer(lst):
        '''
        Finds largest negative integer in a list.
        '''
        negative_integers = []
        for i in lst:
            if i < 0:
                negative_integers.append(i)
        try:
            return max(negative_integers)
        except:
            return None

    def smallest_integer(lst):
        '''
        Finds smallest positive integer in a list.
        '''
        positive_integers = []
        for i in lst:
            if i > 0:
                positive_integers.append(i)
        try:
            return min(positive_integers)
        except:
            return None

    return (largest_integer(lst), smallest_integer(lst))

