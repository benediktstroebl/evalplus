
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
    def comp(a, b):
        if a is None or b is None:
            return a is None, b is None
        if a < b:
            return b, a
        return a, b

    result = min(comp(None, i) for i in lst)
    if result:
        return result

    return (None, None)

    # -1:2:2:2:...
    #  0: 2: 0:2:0:2:0:2:
    #   1: 2: 1:1: 1:2:1:2:

    # i=-1
    # for v in lst:
    #     if v < 0:
    #         i -= 1
    #         if i < 0:
    #             return v, None

    # i = len(lst) - 1
    # for v in lst:
    #     if v >= 0:
    #         i -= 1
    #         if i < 0:
    #             return None, v

    # return None, None

    # # An easier solution without nesting
    # return max(filter(None, (max(v for v in lst if v < 0)
    #                          for v in lst if v >= 0)),
    #            key=lambda x: (x is None, x))

    # # A Pythonic solution
    # zero = min(v for v in lst if v < 0)
    # if zero is None:
    #     return None, None
    # return max(filter(None, (min(v for v in lst if v >=0) for v in lst)),
    #            key=lambda x: (x is None, x))

    # # The other solution that uses the stateful nature of Python's map
    # # to return the most negative integer
    # result = None
    # for x in lst:
    #     if x < 0 and (result is None or x > result):
    #         result = x
    # return result, None

