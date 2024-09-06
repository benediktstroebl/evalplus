
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
    negative_lst_index = []
    positive_lst_index = []
    result = []

    for i in lst:
        if i < 0:
            negative_lst_index.append(i)
        elif i > 0:
            positive_lst_index.append(i)

    if not negative_lst_index and not positive_lst_index:
        result = (None, None)
    elif not negative_lst_index and positive_lst_index:
        result = (min(positive_lst_index), max(positive_lst_index))
    elif not positive_lst_index and negative_lst_index:
        result = (min(negative_lst_index), max(negative_lst_index))
    elif positive_lst_index and negative_lst_index:
        result = (min(min(negative_lst_index), min(positive_lst_index)), max(max(positive_lst_index), max(negative_lst_index)))

    return result
