
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

    # the code below would solve the problem, but uses a bit more memory.
    # because we are only interested in the integers, we can ignore the other
    # values in the list.
    #
    # negative = []
    # positive = []
    # for item in lst:
    #     if isinstance(item, int):
    #         if item < 0:
    #             negative.append(item)
    #         else:
    #             positive.append(item)
    #
    # return (max(negative) if negative else None,
    #         min(positive) if positive else None)

    # using the same principle, but saving the memory by only iterating
    # through the list once.
    negative = None
    positive = None
    for item in lst:
        if isinstance(item, int):
            if item < 0:
                if negative is None:
                    negative = item
                else:
                    negative = max(negative, item)
            elif positive is None:
                positive = item
            else:
                positive = min(positive, item)

    return (negative, positive)

