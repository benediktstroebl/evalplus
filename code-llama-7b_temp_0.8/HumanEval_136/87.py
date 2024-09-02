
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
    positive_nums = []
    negative_nums = []

    for num in lst:
        if num > 0:
            positive_nums.append(num)
        elif num < 0:
            negative_nums.append(num)

    return (max(negative_nums) if negative_nums else None, min(positive_nums) if positive_nums else None)

