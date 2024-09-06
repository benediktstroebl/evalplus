
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

    # for num in lst:
    #     if num >= 0:
    #         smallest = num
    #     if num < 0:
    #         largest = num

    # if smallest!= None and largest!= None:
    #     return (largest, smallest)
    # elif largest == None:
    #     return (None, smallest)
    # elif smallest == None:
    #     return (largest, None)
    # else:
    #     return (None, None)

    def largest_smallest(lst):
        largest = None
        smallest = None
        for num in lst:
            if num >= 0:
                if smallest == None:
                    smallest = num
                else:
                    if num < smallest:
                        smallest = num
            if num < 0:
                if largest == None:
                    largest = num
                else:
                    if num > largest:
                        largest = num
        if smallest == None or largest == None:
            return (None, None)
        else:
            return (largest, smallest)

    return largest_smallest(lst)
