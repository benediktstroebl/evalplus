
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
    return_value = (None, None)
    if lst:
        negative_num = 0
        positive_num = 0
        for num in lst:
            if num < 0:
                negative_num += 1
            else:
                positive_num += 1

        if negative_num > positive_num:
            return_value = (-num, None)
        elif negative_num < positive_num:
            return_value = (None, num)

    return return
