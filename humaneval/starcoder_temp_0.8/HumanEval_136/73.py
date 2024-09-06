
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
    # your code here
    smallest_num = None
    largest_num = None

    for num in lst:
        if num < 0 and smallest_num == None:
            smallest_num = num
        elif num > 0 and largest_num == None:
            largest_num = num
        elif num < 0 and smallest_num!= None:
            smallest_num = min(smallest_num, num)
        elif num > 0 and largest_num!= None:
            largest_num = max(largest_num, num)

    return (largest_num, smallest_num)
