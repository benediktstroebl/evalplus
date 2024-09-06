
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
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] < 0 < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    for i in range(n):
        if lst[i] > 0 > lst[n - i - 1]:
            lst[n - i - 1], lst[i] = lst[i], lst[n - i - 1]

    return (lst[0], lst[n - 1])

