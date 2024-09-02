
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
    # Write your code here.
    sorted_list = sorted(lst)
    for i in sorted_list:
        if i < 0:
            if largest == None or largest < i:
                largest = i
    for i in sorted_list:
        if i > 0:
            if smallest == None or smallest > i:
                smallest = i

    return largest, smallest
