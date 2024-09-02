
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
    negative_count = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            negative_count += 1
    if negative_count == len(lst):
        return None, None

    negative_integers = [i for i in range(len(lst)) if lst[i] < 0]
    positive_integers = [i for i in range(len(lst)) if lst[i] >= 0]

    return min(negative_integers), max(positive_integers
