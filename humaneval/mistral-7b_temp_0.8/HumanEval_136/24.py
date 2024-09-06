
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
    def largest_smallest_integers(lst):
        neg_smallest = None
        pos_largest = None
        for num in lst:
            if num < 0 and neg_smallest == None:
                neg_smallest = num
            if num < 0 and neg_smallest > num:
                neg_smallest = num
            if num > 0 and pos_largest == None:
                pos_largest = num
            if num > 0 and pos_largest < num:
                pos_largest = num
        if neg_smallest == None:
            return (None, None)
        if pos_largest == None:
            return (neg_smallest, None)
        else:
            return (neg_smallest, pos_largest)

    return largest_smallest_integers(lst)

