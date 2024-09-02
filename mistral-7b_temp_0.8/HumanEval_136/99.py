
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
    lst = [int(x) for x in lst]
    if len(lst) == 0:
        return (None, None)
    else:
        if len(lst) == 1:
            return (None, lst[0])
        else:
            negative = []
            positive = []
            for i in lst:
                if i >= 0:
                    positive.append(i)
                else:
                    negative.append(i)
            if len(negative) > 0:
                largest = max(negative)
                smallest = min(positive)
                return (largest, smallest)
            else:
                return (None, None)
