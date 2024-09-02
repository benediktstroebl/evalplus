
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
    ans = None, None
    for x in lst:
        if x < 0:
            if ans[0] is None:
                ans = x, ans[1]
            else:
                ans = max(ans[0], x), min(ans[1], x)
        elif x > 0:
            if ans[1] is None:
                ans = ans[0], x
            else:
                ans = max(ans[0], ans[1]), x
    return ans
