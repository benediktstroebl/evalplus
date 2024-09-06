
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

    if(len(lst) == 0):
        return(None, None)
    elif(len(lst) == 1):
        if(lst[0] < 0):
            return(lst[0], None)
        else:
            return(None, lst[0])
    else:
        largest = None
        smallest = None
        for x in lst:
            if(x < 0 and largest == None):
                largest = x
            elif(x < 0):
                largest = max(x, largest)
            if(x > 0 and smallest == None):
                smallest = x
            elif(x > 0):
                smallest = min(x, smallest)
        if(largest == None):
            return(None, smallest)
        elif(smallest == None):
            return(largest, None)
        else:
            return(largest, smallest)

